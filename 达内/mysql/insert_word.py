"""
将单词本存入数据库

1. 创建数据库dict （utf8）
2. 创建数据表words 将单词和单词解释分别存入不同的字段
    create table words(id int primary key auto_increment,word char(32),mean text);
3.将单词存入words单词表 超过19500即可
"""
import pymysql
import re


f = open('dict.txt')

# 连接数据库
db = pymysql.connect(host= 'localhost',
                     port = 3306,
                     user= 'root',
                     passwd = '03241214',
                     database= 'dict',
                     charset = 'utf8')

# 获取游标（操作数据库，执行sql语句）
cur = db.cursor()
sql = "insert into words (word,mean) values (%s,%s)"

for line in f:
    # 获取单词和解释
    tup = re.findall(r'(\S+)\s+(.*)',line)[0]
    try:
        cur.execute(sql, tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)

f.close()
cur.close()
db.close()

