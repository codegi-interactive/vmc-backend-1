#!/bin/bash

# Wait for MySQL to be ready
echo "Waiting for MySQL..."
while ! nc -z $MYSQL_HOST 3306; do
  sleep 1
done
echo "MySQL is ready!"

# Wait for Redis to be ready
echo "Waiting for Redis..."
while ! nc -z $REDIS_HOST 6379; do
  sleep 1
done
echo "Redis is ready!"

# 安装必要的包
echo "Installing required packages..."
apt-get update && apt-get install -y netcat-openbsd

# 使用强健的遷移脚本初始化數據庫
echo "執行强健的數據庫遷移..."
python robust_migrations.py

# Create admin user
echo "Creating/updating admin user..."
python insert_admin.py

# Start the application
echo "Starting application..."
python manage.py runserver 0.0.0.0:8000 