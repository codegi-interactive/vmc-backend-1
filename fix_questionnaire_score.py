#!/usr/bin/env python
import os
import django
import logging
import sys
from django.db import connections, OperationalError, ProgrammingError

# 設置日誌
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("fix_questionnaire_score")

# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmc_backend.settings')
django.setup()

def check_table_exists(table_name):
    """檢查表是否存在"""
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            return cursor.fetchone() is not None
    except Exception as e:
        logger.warning(f"檢查表 {table_name} 是否存在時出錯: {e}")
        return False

def execute_sql(sql, params=None):
    """執行SQL語句"""
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(sql, params)
            return True
    except Exception as e:
        logger.error(f"執行SQL語句出錯: {e}")
        return False

def fix_questionnaire_score_tables():
    """修復問卷評分相關表"""
    # 檢查表是否存在
    if check_table_exists('questionnaire_score_info'):
        logger.info("檢测到questionnaire_score_info表已存在")
        
        # 確認migration表
        if not check_table_exists('django_migrations'):
            logger.error("django_migrations表不存在，無法修復遷移狀態")
            return False
        
        try:
            # 檢查問卷評分的遷移是否已應用
            with connections['default'].cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM django_migrations 
                    WHERE app='questionnaire_score' 
                    AND name='0002_questionnairescoreinfo_and_more'
                """)
                migration_exists = cursor.fetchone() is not None
            
            if migration_exists:
                logger.info("遷移 questionnaire_score.0002_questionnairescoreinfo_and_more 已應用")
            else:
                logger.info("遷移 questionnaire_score.0002_questionnairescoreinfo_and_more 未應用，正在添加...")
                
                # 手動添加遷移記錄
                successful = execute_sql("""
                    INSERT INTO django_migrations (app, name, applied) 
                    VALUES ('questionnaire_score', '0002_questionnairescoreinfo_and_more', NOW())
                """)
                
                if successful:
                    logger.info("已成功添加遷移記錄")
                else:
                    logger.error("添加遷移記錄失敗")
                    return False
            
            return True
            
        except (OperationalError, ProgrammingError) as e:
            logger.error(f"數據庫操作錯誤: {e}")
            return False
    else:
        logger.info("questionnaire_score_info表不存在，不需要修復")
        return True

def fix_user_info_table():
    """嘗試修復user_info表問題"""
    if not check_table_exists('user_info') and check_table_exists('auth_user'):
        logger.info("user_info表不存在但auth_user表存在，嘗試手動創建user_info表...")
        
        # 這裡需要根據實際的表結構定義正確的CREATE TABLE語句
        # 以下是一個示例，實際應用中需要替换為正確的表結構
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS `user_info` (
          `id` varchar(64) NOT NULL,
          `username` varchar(20) NOT NULL,
          `password` varchar(50) NOT NULL,
          `email` varchar(50) DEFAULT NULL,
          `phone` varchar(20) DEFAULT NULL,
          `farm_name` varchar(50) DEFAULT NULL,
          `sex` char(1) DEFAULT NULL,
          `last_logon_time` varchar(50) DEFAULT NULL,
          `is_admin` char(1) DEFAULT NULL,
          `status` char(1) DEFAULT NULL,
          `create_time` varchar(50) DEFAULT NULL,
          `create_by` varchar(50) DEFAULT NULL,
          `update_time` varchar(50) DEFAULT NULL,
          `update_by` varchar(50) DEFAULT NULL,
          `deleted` char(1) DEFAULT '0',
          PRIMARY KEY (`id`),
          UNIQUE KEY `username` (`username`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        
        if execute_sql(create_table_sql):
            logger.info("已成功創建user_info表")
            
            # 標記遷移為已應用
            if execute_sql("""
                INSERT INTO django_migrations (app, name, applied) 
                VALUES ('user', '0001_initial', NOW())
            """):
                logger.info("已成功添加user遷移記錄")
                return True
            else:
                logger.error("添加user遷移記錄失敗")
                return False
        else:
            logger.error("創建user_info表失敗")
            return False
    else:
        logger.info("user_info表已存在或auth_user表不存在，不需要修復")
        return True

if __name__ == "__main__":
    logger.info("開始修復問卷評分和用户相關表...")
    
    # 修復問卷評分表
    if fix_questionnaire_score_tables():
        logger.info("問卷評分表修復成功")
    else:
        logger.error("問卷評分表修復失敗")
        sys.exit(1)
    
    # 修復用户表
    if fix_user_info_table():
        logger.info("用户表修復成功")
    else:
        logger.error("用户表修復失敗")
        sys.exit(1)
    
    logger.info("所有修復完成")
    sys.exit(0) 