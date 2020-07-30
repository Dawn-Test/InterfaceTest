"""
目标：get 请求方法带参演练
案例：
    1.http：//www.baidu.com？id=1001
    2.http：//www.baidu.com？id=1001,1002
    3.http：//www.baidu.com？id=1001&kw=北京
请求:
    请求方法 ：get
参数：
    params：字典或字符串 （推荐使用字典）
相应：
    1.相应对象.url            获取请求url
    2.相应对象.status_code    获取相应状态码信息
    3.相应对象.text           以文本形式获取相应信息
"""


# 导包
import requests

# 调用get
url = "http://www.baidu.com"
# 不推荐方法  静态
# url = "http://www.baidu.com？id=1001"

# 案例一  定义字典
# params = {"id": 1001}

# 案例二 定义字典
# params = {"id": [1001 , 1002]}  # 不推荐
# params = {"id": "1001 , 1002"}    # %2c ASCI值为逗号

# 案例三
params = {"id": 1001, "kw": "北京"}    # 多个键值使用参数
# 请求带参 params
r = requests.get(url, params=params)

# 获取请求url地址
print("请求url：", r.url)

# 获取相应状态码信息
print("状态码：", r.status_code)

# 获取相应信息  以文本形式
print("以文本相应内容：", r.text)