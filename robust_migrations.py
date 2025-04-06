#!/usr/bin/env python
import os
import django
import subprocess
import sys
import time
import logging
from django.db import connections, OperationalError, ProgrammingError

# 設置日誌
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("robust_migrations")

# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmc_backend.settings')
django.setup()

def wait_for_db():
    """等待數據庫可用"""
    logger.info("等待數據庫連接...")
    db_conn = None
    retry_count = 0
    max_retries = 30
    
    while retry_count < max_retries:
        try:
            db_conn = connections['default']
            db_conn.cursor()
            logger.info("數據庫連接成功!")
            return True
        except OperationalError:
            retry_count += 1
            logger.info(f"數據庫未就緒，等待重試... ({retry_count}/{max_retries})")
            time.sleep(2)
    
    logger.error("無法連接到數據庫，退出!")
    return False

def get_app_names():
    """獲取所有應用名稱"""
    from django.apps import apps
    app_configs = apps.get_app_configs()
    return [app.name for app in app_configs 
            if not app.name.startswith('django.') 
            and not app.name.startswith('rest_framework')]

def make_migrations(app_names):
    """為所有應用創建遷移文件"""
    logger.info("為所有應用創建遷移文件...")
    for app_name in app_names:
        logger.info(f"為應用 {app_name} 創建遷移文件...")
        try:
            subprocess.run([sys.executable, 'manage.py', 'makemigrations', app_name], 
                         check=False, capture_output=True, text=True)
        except Exception as e:
            logger.warning(f"為應用 {app_name} 創建遷移文件時出錯: {e}")

def check_table_exists(table_name):
    """檢查表是否存在"""
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            return cursor.fetchone() is not None
    except Exception as e:
        logger.warning(f"檢查表 {table_name} 是否存在時出錯: {e}")
        return False

def migrate_app(app_name, fake_if_table_exists=None, options=None):
    """遷移單個應用
    
    Args:
        app_name: 應用名稱
        fake_if_table_exists: 如果該表存在，則使用--fake參數
        options: 附加的遷移選項
    """
    cmd = [sys.executable, 'manage.py', 'migrate', app_name]
    
    # 如果指定了表名，並且該表已存在，使用--fake選項
    if fake_if_table_exists and check_table_exists(fake_if_table_exists):
        logger.info(f"表 {fake_if_table_exists} 已存在，將使用--fake參數")
        cmd.append('--fake')
    
    # 添加額外選項
    if options:
        cmd.extend(options)
    
    logger.info(f"執行命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
        if result.returncode == 0:
            logger.info(f"應用 {app_name} 遷移成功")
            return True
        else:
            logger.warning(f"應用 {app_name} 遷移出錯: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"執行遷移命令時出錯: {e}")
        return False

def robust_migrate():
    """執行强健的遷移流程"""
    if not wait_for_db():
        return False
    
    # 獲取所有應用
    app_names = get_app_names()
    logger.info(f"發現以下應用需要遷移: {', '.join(app_names)}")
    
    # 創建遷移文件
    make_migrations(app_names)
    
    # 首先嘗試運行完整遷移
    logger.info("嘗試完整遷移...")
    try:
        result = subprocess.run([sys.executable, 'manage.py', 'migrate'],
                              check=False, capture_output=True, text=True)
        
        # 如果成功，直接返回
        if result.returncode == 0:
            logger.info("數據庫遷移成功完成！")
            return True
        
        # 如果失敗，解析錯誤消息
        error_msg = result.stderr
        logger.warning(f"完整遷移失敗: {error_msg}")
        
        # 檢查是否有表已存在的錯誤
        if "already exists" in error_msg:
            logger.info("檢测到表已存在錯誤，嘗試逐個應用遷移...")
            
            # 先處理基础表
            base_apps = ['contenttypes', 'auth', 'admin', 'sessions']
            for app in base_apps:
                migrate_app(app, options=['--fake-initial'])
            
            # 逐個處理其他應用
            for app_name in app_names:
                # 嘗試普通遷移
                if not migrate_app(app_name):
                    # 如果失敗，嘗試使用--fake-initial
                    logger.info(f"嘗試使用--fake-initial遷移 {app_name}")
                    migrate_app(app_name, options=['--fake-initial'])
            
            logger.info("逐個應用遷移完成")
            
            # 最後再嘗試一次完整遷移，以應用可能遗漏的依赖
            logger.info("最後一次嘗試完整遷移...")
            final_result = subprocess.run([sys.executable, 'manage.py', 'migrate'],
                                       check=False, capture_output=True, text=True)
            
            if final_result.returncode == 0:
                logger.info("數據庫遷移最終成功完成！")
                return True
            else:
                logger.warning(f"最終遷移仍然失敗: {final_result.stderr}")
                return False
        
        # 處理缺少表的錯誤
        elif "doesn't exist" in error_msg:
            logger.info("檢测到表不存在錯誤，嘗試使用--fake-initial...")
            
            # 嘗試使用--fake-initial
            for app_name in app_names:
                migrate_app(app_name, options=['--fake-initial'])
            
            return True
    
    except Exception as e:
        logger.error(f"執行遷移過程中出錯: {e}")
        return False
    
    return False

def fix_specific_issues():
    """修復已知的特定問題"""
    # 修復問卷評分表問題
    if check_table_exists('questionnaire_score_info'):
        logger.info("檢测到questionnaire_score_info表已存在，使用--fake遷移")
        migrate_app('questionnaire_score', 'questionnaire_score_info', ['--fake'])
    
    # 修復用户表問題
    if not check_table_exists('user_info') and check_table_exists('auth_user'):
        logger.info("檢测到user_info表不存在但auth_user存在，嘗試修復")
        migrate_app('user', options=['--fake-initial'])

if __name__ == "__main__":
    logger.info("開始執行强健的數據庫遷移...")
    
    # 先嘗試修復已知的特定問題
    fix_specific_issues()
    
    # 執行强健的遷移
    if robust_migrate():
        logger.info("强健的數據庫遷移完成!")
    else:
        logger.error("强健的數據庫遷移失敗!")
        sys.exit(1) 