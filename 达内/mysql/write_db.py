"""
write.py
pymysql 写操作示例(insert update delete)
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

# 写数据库
try:
    # 写sql语句执行
    # 插入操作
    # name = input('Name:')
    # age = input("Age:")
    # socre = input("Score:")

    # 将变量插入到sql语句合成最终操作
    #sql = "insert into class (name,age,socre) values(‘%s’,%s,%s)" % (name,age,socre)

    # 可以使用列表直接给sql语句的values传值
    # sql = "insert into class (name,age,socre) values(%s,%s,%s)"
    # cur.execute(sql,[name,age,socre])  # 执行语句

    # 修改操作
    # sql = "update interest set price = 11800 where name='Tom';"
    # cur.execute(sql)

    # 删除操作
    sql = "delete from class where socre<90;"
    cur.execute(sql)
    db.commit()  # 将写操作提交，多次写操作一同提交

except Exception as e:
    db.rollback() # 退回到commit执行之前的数据库状态
    print(e)


# 关闭数据库
cur.close()
db.close()