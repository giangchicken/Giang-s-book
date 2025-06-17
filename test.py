from sqlalchemy import create_engine

# Thay thế 'username' và 'password' bằng thông tin thực tế
username = 'dungnv'
password = 'Abc@4321'
host = '192.168.25.51'
port = 3306
database = 'v3m'

# # Tạo connection string
# connection_string = f"mariadb+pymysql://{username}:{password}@{host}:{port}/{database}"

import pymysql

# Thay thế 'username' và 'password' bằng thông tin thực tế
connection = pymysql.connect(
    host='192.168.25.51',
    port=3306,
    user=username,
    password=password,
    database='v3m'
)

with connection.cursor() as cursor:
    cursor.execute("SELECT  FROM company_addr")
    result = cursor.fetchone()
    print(result)

connection.close()

# # Tạo engine
# engine = create_engine(connection_string)

# # Kiểm tra kết nối
# with engine.connect() as connection:
#     result = connection.execute("SELECT 10")
#     print(result.fetchone())