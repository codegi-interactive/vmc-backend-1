#!/usr/bin/env python
import os
import django

# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmc_backend.settings')
django.setup()

from farm_home.models import FarmHomeInfo
from django.db import connection

# 需要修復的主鍵IDs
problematic_ids = [
    '1aa2bd8f13d84c379b83efda59023394',
    'c4a142f77ad14b648fecb37419d578e8'
]

print("開始修復farm_home_info表中的主鍵冲突...")

# 檢查每個ID並嘗試修復
for pid in problematic_ids:
    records = FarmHomeInfo.objects.filter(id=pid)
    count = records.count()
    
    if count > 0:
        print(f"找到ID為 {pid} 的記錄 {count} 條，删除中...")
        
        # 為確保安全，使用原始SQL删除記錄
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM farm_home_info WHERE id = '{pid}'")
            print(f"已從數據庫中删除ID為 {pid} 的記錄")
    else:
        print(f"未找到ID為 {pid} 的記錄，無需修復")

print("修復完成！")

# 在prod環境中還應修復farm_home/views.py中的add方法，
# 應使用get_uuid_str()生成新ID，而不是重用現有ID
print("注意：為了永久解决此問題，建議修改farm_home/views.py中的add方法，確保每次都生成新的UUID") 