"""
目标：pymysql完成新增数据操作
案例：
    新增一条图书
sql：
    insert into t_book(title,pub_date) values("西游记",“1980-1-3”)
"""
# 导包
import pymysql
# 获取数据库连接对象
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="588588",
                       database="books",
                       port=3306,
                       autocommit=True)

# 获取游标对象
cursor = conn.cursor()
# 调用执行方法
sql = "text15_新增记录操作.py"
cursor.execute(sql)
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()