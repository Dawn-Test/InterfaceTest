"""
目标：pymysql完成新增数据操作
案例：
    更新西游记阅读量增加1
sql：
    update  t_book set `read'=`read`+1 where title='西游记'
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
sql = "update  t_book set `read`=`read`+1 where title='西游记'"
cursor.execute(sql)
# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()