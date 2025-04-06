import os

# redis配置
redis_conf_localhost = os.environ.get("REDIS_HOST", "localhost")
redis_conf_password = "Spinfo@0123"
# redis_conf_password = ""
redis_conf_port = "6379"
redis_conf_dbname = "0"
# 緩存超時事件,單位:秒
redis_conf_cache_time = 60 * 60 * 8

# mysql配置
mysql_conf_localhost = os.environ.get("MYSQL_HOST", "localhost")
mysql_conf_username = "root"
# mysql_conf_password = ""
mysql_conf_password = "QAZwsx123..MySql"
mysql_conf_port = "3306"
mysql_conf_dbname = "db1"

# file配置

# 文件上傳後的存儲路徑
file_root = "/opt/data/"

# 郵件配置
email_host = 'smtp.qq.com'
email_port = 465
email_host_user = '1752476835@qq.com'
email_host_password = 'nlkxrfrsteoaddhd'

# 郵件發送標題
email_register_send_template_title = "OHRP-注冊驗証碼"
email_reset_password_send_template_title = "OHRP-重置密碼驗証碼"
# 郵件發送内容， 格式為 内容***{}***内容，{}會填充驗証碼，形成完成的郵件内容。
# 例
# 模板 = 【這是登錄的驗証碼，驗証碼{}】，驗証碼 = 1234
# 實際發送的郵件内容 =  【這是登錄的驗証碼，驗証碼1234】
email_send_template_content = "這是登錄的驗証碼，驗証碼内容 = {}"

# 驗証碼是否全部是數字
code_type_digit = True

# 啟用單點登錄功能
single_sign_on = True
