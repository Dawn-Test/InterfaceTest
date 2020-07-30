"""
目标：post 请求方法演练
案例：新增学院
请求:
    请求方法 ：post
参数：
    1.json：传入json字符串
    2.headers 传入请求头内容
响应：
    1.响应对象.json（）
"""


# 导包
import requests

# 调用post
url = "http://www.baidu.com"
r = requests.post(url)   # r：为响应数据对象

# 请求url
url = "http://127.0.0.1:8000/api/departments/"

# 请求headers
headers = {"Content-Type": "application/json"}

# 请求json
data = {
        "data": [{
                    "dep_id": "T01",
                    "dep_name": "Test学院",
                    "master_name": "Test-Master",
                    "slogan": "Here is Slogan"
        }]
        }
requests.post(url, json=data, headers=headers)
# 获取响应对象
print(r.json())

# 获取相应状态码信息
print("状态码：", r.status_code)
