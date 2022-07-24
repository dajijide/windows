"""
pymysql 操作数据库演示流程
"""

import pymysql

# 连接数据库
db = pymysql.connect(host= 'localhost',
                     port = 3306,
                     user= 'root',
                     passwd = '03241214',
                     database= 'stu',
                     charset = 'utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()

# 执行sql语句
sql = "insert into class values(5,'Emma',20,'w',95,'2022-7-1');"

cur.execute(sql) # 执行语句
db.commit() # 将写操作提交，多次写操作一同提交

# 关闭数据库
cur.close()
db.close()