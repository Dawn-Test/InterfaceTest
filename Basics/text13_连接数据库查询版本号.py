"""
目标：连接数据库查询数据库版本号
相关方法：
    sql语句：select version（）
    连接对象： pumysql.connect（参数）
    获取游标： cursor = 连接对象.cursor（）
    执行SQL语句方法：游标对象.execute（sql）
    获取单条结果：游标对象.fetchone（）
    关闭游标及连接：游标对象.close（）连接.close（）
"""
# 导包 pumysql
import pymysql

# 获取数据库连接对象 必填对象
# conn = pymysql.connect(host="localhost",
#                        user="root",
#                        password="588588",
#                        database="books",
#                        port=3306,
#                        charset="utf8",
#                        autocommit=False)
# # print(conn)
conn = pymysql.connect("127.0.0.1",
                       "root",
                       "588588",
                       "books",
                       3306,
                       charset="utf8"
                       )


# 获取游标对象
a = conn.connect()
# print(cursor)

# 调用执行方法/获取数据方法
sql = "select version()"
num = a.execure(sql)
print("执行的结果为：", num)

# 获取执行结果
result_one = a.fetchone()
print("获取的执行结果为：", result_one)
# 关闭游标对象
a.close()
# 关闭链接对象
conn.close()