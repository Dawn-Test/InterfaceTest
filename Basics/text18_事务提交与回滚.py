"""
目标：pymysql完成新增数据操作
案例：
    新增一条图书数据
        sql：insert into t_book(title,pub_date) values("西游记",“1980-1-3”)
    新增一条英雄人物
        sql：insert into t_hero(name,gender,book_id) values("孙悟空",1,4)
方法：
    自动提交事务方法 连接对象.autocommit（True）
    手动提交事务方法 连接对象.commit（）
    事务回滚方法 连接对象.rollback（）
"""
# 导包
import pymysql
# 获取数据库连接对象
conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="588588",
                       database="books",
                       port=3306)

# 获取游标对象
cursor = conn.cursor()

# 自动提交事务（通过方法）
conn.autocommit(True)   # true  开启自动提交
# 新增图书
sql_book = "insert into t_book(id,title,pub_date) values ('4','东游记','1980-1-3')"
cursor.execute(sql_book)

# 新增英雄人物
sql_hero = "insert into t_hero(id,name,gender,book_id) values(6,'孙悟空',1,4)"
cursor.execute(sql_hero)

# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()