"""
目标：post 请求方法演练   参数（data和json区别）
案例：新增学院
将词典对象转换成json字符串：
    1.导入json
    2.dumps（dict）
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
import json

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
# 使用json 方式新增学院 -->成功
# requests.post(url, json=data, headers=headers)

# 使用data 方式新增学院 -->失败  注意：对python字典和json虽然长得一样
#                                   但是数据序列化格式还是有一定区别
# requests.post(url, data=data, headers=headers)

# 将字典对象转为json字符串
requests.post(url, data=json.dumps(data), headers=headers)
# 获取响应对象
print(r.json())

# 获取相应状态码信息
print("状态码：", r.status_code)
