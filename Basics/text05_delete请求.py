"""
目标：post 请求方法演练  delete方法
案例：删除新增学院
请求:
    请求方法 ：post
响应：
    1.响应状态码 204
"""


# 导包
import requests

# 调用post
url = "http://www.baidu.com"
r = requests.post(url)   # r：为响应数据对象

# 请求url
url = "http://127.0.0.1:8000/api/departments/T01"
r = requests.delete(url)

print("状态码：", r.status_code)
