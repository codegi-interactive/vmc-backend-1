#!/usr/bin/env python
import os
import django
import hashlib
import logging
import sys
from django.db import OperationalError, ProgrammingError

# 設置日誌
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("insert_admin")

# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmc_backend.settings')
django.setup()

def check_table_exists(table_name):
    """檢查表是否存在"""
    from django.db import connections
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            return cursor.fetchone() is not None
    except Exception as e:
        logger.warning(f"檢查表 {table_name} 是否存在時出錯: {e}")
        return False

# MD5加密函數，與系统中使用的相同
def md5_encrypt(password):
    return hashlib.new('md5', bytes(password, encoding='utf-8')).hexdigest()

def create_admin_user():
    try:
        from user.models import UserInfo
        from django.db.models import Q
        from common.time_utils import get_format_time

        logger.info(f"密碼 '12345678' 的MD5哈希值: {md5_encrypt('12345678')}")

        # 檢查用户表是否存在
        if not check_table_exists('user_info'):
            logger.error("user_info表不存在，無法創建管理員用户")
            return False

        # 檢查用户是否已存在
        try:
            admin_exists = UserInfo.objects.filter(Q(username='sysadmin')).exists()
            
            if admin_exists:
                logger.info("管理員用户 'sysadmin' 已存在，正在更新密碼...")
                UserInfo.objects.filter(Q(username='sysadmin')).update(
                    password=md5_encrypt('12345678')
                )
                logger.info("密碼已更新")
            else:
                logger.info("正在創建管理員用户...")
                # 創建新管理員用户
                UserInfo.objects.create(
                    id='42d83d66fdf0451db16c3fe434f09e61',
                    username='sysadmin',
                    password=md5_encrypt('12345678'),  # 使用MD5加密的密碼
                    email='1752476831@qq.com',
                    phone='+825223436781',
                    farm_name='Lau',
                    sex='0',
                    last_logon_time='',
                    is_admin='1',
                    status='1',
                    create_time=get_format_time(),
                    create_by='sysadmin',
                    update_time=get_format_time(),
                    update_by='sysadmin',
                    deleted='0'
                )
                logger.info("管理員用户創建成功")

            logger.info(f"用户名: sysadmin")
            logger.info(f"密碼: 12345678")
            logger.info(f"密碼MD5值: {md5_encrypt('12345678')}")
            return True
        
        except (OperationalError, ProgrammingError) as e:
            logger.error(f"數據庫操作錯誤: {e}")
            return False
            
    except ImportError as e:
        logger.error(f"導入模塊錯誤: {e}")
        return False
    except Exception as e:
        logger.error(f"創建管理員用户時出錯: {e}")
        return False

if __name__ == "__main__":
    logger.info("開始創建/更新管理員用户...")
    
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        if create_admin_user():
            logger.info("管理員用户處理完成")
            sys.exit(0)
        else:
            retry_count += 1
            if retry_count < max_retries:
                logger.warning(f"創建管理員用户失敗，將重試 ({retry_count}/{max_retries})...")
            else:
                logger.error("創建管理員用户失敗，已達到最大重試次數")
    
    # 如果重試都失敗了，但不想因此阻止應用啟動，可以選擇正常退出
    # 如果希望在管理員創建失敗時阻止應用啟動，則取消下面的注釋
    # sys.exit(1) 