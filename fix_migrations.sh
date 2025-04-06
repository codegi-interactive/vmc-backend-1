#!/bin/bash

echo "VMC Backend - 遷移修復工具"
echo "=========================="
echo

# 1. 首先嘗試特定問題修復
echo "正在修復特定問題..."
python fix_questionnaire_score.py
if [ $? -ne 0 ]; then
    echo "特定問題修復失敗，嘗試继續..."
fi

# 2. 運行强健的遷移脚本
echo "正在執行强健的數據庫遷移..."
python robust_migrations.py
if [ $? -ne 0 ]; then
    echo "强健的數據庫遷移失敗"
    exit 1
fi

# 3. 嘗試創建管理員用户
echo "正在創建/更新管理員用户..."
python insert_admin.py
if [ $? -ne 0 ]; then
    echo "警告: 管理員用户創建失敗，但將继續執行"
fi

echo "修復完成！"
echo "如果應用仍有問題，可能需要重置數據庫:"
echo "  docker-compose down"
echo "  docker volume rm vmc-backend_mysql_data"
echo "  docker-compose up -d" 