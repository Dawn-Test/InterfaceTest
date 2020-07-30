"""
目标：post 请求方法演练
    响应对象.text与响应对象.json（）区别
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
# 获取响应对象  json形式
r_json = r.json()
print("r_json:", r_json)
print("r_json类型：", type(r_json))
print("r_json通过键名获取值：", r_json("already_exist"))

# 获取响应对象  text形式
r_text = r.text
print("r_text:", r_text)
print("r_text类型：", type(r_text))
# 预期结果 报错 因为字符串没有键名一说
print("r_text通过键名获取值：", r_text("already_exist"))

# 获取相应状态码信息
print("状态码：", r.status_code)
