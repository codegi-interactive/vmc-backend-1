#!/usr/bin/env python
import os
import django
import subprocess
import sys

# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmc_backend.settings')
django.setup()

print("開始初始化數據庫...")

# 獲取所有應用
from django.apps import apps
app_configs = apps.get_app_configs()
app_names = [app.name for app in app_configs if not app.name.startswith('django.') and not app.name.startswith('rest_framework')]

print(f"發現以下應用需要遷移: {', '.join(app_names)}")

# 為每個應用創建遷移文件
for app_name in app_names:
    print(f"為應用 {app_name} 創建遷移文件...")
    try:
        subprocess.run([sys.executable, 'manage.py', 'makemigrations', app_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"為應用 {app_name} 創建遷移文件時出錯: {e}")

# 應用所有遷移
print("應用所有遷移...")
try:
    subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
    print("數據庫遷移成功完成！")
except subprocess.CalledProcessError as e:
    print(f"應用遷移時出錯: {e}") 