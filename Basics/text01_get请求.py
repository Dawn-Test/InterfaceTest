"""
目标：get 请求方法演练
案例：http：//www.baidu.com
请求:
    请求方法 ：get
相应：
    1.相应对象.url            获取请求url
    2.相应对象.status_code    获取相应状态码信息
    3.相应对象.text           以文本形式获取相应信息
"""


# 导包
import requests

# 调用get
url= "http://www.baidu.com"
r = requests.get(url)   # r：为响应数据对象

# 获取请求url地址
print("请求url：", r.url)

# 获取相应状态码信息
print("状态码：", r.status_code)

# 获取相应信息  以文本形式
print("以文本相应内容：", r.text)

