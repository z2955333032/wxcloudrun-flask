import os

# 是否开启debug模式
DEBUG = True

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", 'root')
password = os.environ.get("MYSQL_PASSWORD", 'bST3Njt6')
db_address = os.environ.get("MYSQL_ADDRESS", '10.0.224.16:3306')
