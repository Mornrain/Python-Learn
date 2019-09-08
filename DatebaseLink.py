# pycharm连接数据库操作
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
# MySQL8.0以后必须要添加的内容
    auth_plugin='mysql_native_password'
)
mycursor=mydb.cursor()
mycursor.execute('show databases')
for x in mycursor:
    print(x)