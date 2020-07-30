"""
目标：数据库查询演练
需求：
    获取所有图书记录
    获取所有图书名称
    获取前两本图书
相关方法：
    sql语句：select version（）
    所有记录数：游标对象.fowcount 或 游标对象.execute（）返回结果
    所有图书名称：游标对象.fetchall
    指定行数：游标对象.fetchmany(size)
"""
# 导包 pumysql
import pymysql

# 获取数据库连接对象 必填对象

conn = pymysql.connect("127.0.0.1",
                       "root",
                       "588588",
                       "books",
                       3306,
                       charset="utf8"
                       )


# 获取游标对象
a = conn.connect()

# 调用执行方法/获取数据方法
sql = "select * from t_book"
num = a.execute(sql)

# 获取所有图书记录
num = a.rowcount
print("所有图书记录数为：", num)
# 获取所有图书名称
all = a.fetchall()
print("所有图书信息：", all)

# 遍历元组  获取名称
for i in all:
    print("获取的图书名称为：", i[1])
# 获取前两本图书
size = a.fetchmany(2)
print("获取前两挑的数据：", size)
# 关闭游标对象
a.close()
# 关闭链接对象
conn.close()