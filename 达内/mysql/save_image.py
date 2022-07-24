"""
二进制文件存储演示
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

# 存储图片
# with open('image.jpg','rb') as f:
#     data = f.read()
# try:
#     sql = "update class set image = %s where name='James';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 获取图片
sql = "select image from class where name ='James';"
cur.execute(sql)
date=cur.fetchone()
with open('putao.jpg','wb') as f:
    f.write(date[0])

cur.close()
db.close()