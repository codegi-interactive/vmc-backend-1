#!/usr/bin/env python
import os
import sys
import re
import glob

# 項目根目錄
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 要檢查的應用目錄
APP_DIRS = [
    'farm_home', 'immunization', 'clear', 'chicken_flock', 'dict_info', 
    'farm_other_attributes', 'feed_warehouse_capacity', 'fine_feed_dosage',
    'medication_use', 'normal_feed_dosage', 'obituary', 'questionnaire_score',
    'notice', 'commodity', 'order', 'shopp_cart'
]

# 用於匹配重用UUID的正則表達式
UUID_REUSE_PATTERN = r'uuid\s*=\s*get_uuid_str\(\)\s+if\s+.*?\s+else\s+.*?\.id'

# 要修復的模式
FIX_FROM = 'uuid = get_uuid_str() if info is None else info.id'
FIX_TO = '''# 修復: 始終生成新的UUID，而不是重用現有ID
    uuid = get_uuid_str()'''

def check_and_fix_file(file_path):
    """檢查並修復文件中的UUID重用問題"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 檢查是否存在UUID重用問題
    if re.search(UUID_REUSE_PATTERN, content):
        print(f"在文件 {file_path} 中發現UUID重用問題")
        
        # 修復問題
        fixed_content = content.replace(FIX_FROM, FIX_TO)
        
        # 保存修復後的文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"已修復文件 {file_path}")
        return True
    
    return False

def main():
    """檢查並修復所有應用視圖中的UUID重用問題"""
    total_fixed = 0
    
    print("開始檢查並修復UUID重用問題...")
    
    for app_dir in APP_DIRS:
        app_path = os.path.join(BASE_DIR, app_dir)
        if not os.path.exists(app_path):
            print(f"應用目錄 {app_path} 不存在，跳過")
            continue
        
        views_path = os.path.join(app_path, 'views.py')
        if os.path.exists(views_path):
            if check_and_fix_file(views_path):
                total_fixed += 1
    
    print(f"檢查完成，共修復了 {total_fixed} 個文件")
    
    if total_fixed > 0:
        print("\n建議執行以下命令部署修復:")
        print("1. 重啟容器: docker-compose down && docker-compose up -d")
        print("2. 或者在容器内更新代碼: docker exec -it vmc-backend bash -c 'cd /opt/vmc-backend && git pull'")

if __name__ == "__main__":
    main() 