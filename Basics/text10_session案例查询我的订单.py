"""
目标：通过session登录tpshop查询我的订单
案例数据：
    1.获取验证码：http://demo6.tp-shop.cn/index.php?m=Home&c=User&a=verify&r=0.2316697196238724
    2.登录接口：http://demo6.tp-shop.cn/Home/User/index.html
    3.订单：http://demo6.tp-shop.cn/Home/Order/order_list.html
    4.登录数据：
        data = {"username":"15376546286",
        "password":"123123",
        "verify_code":8888}
"""

# 导包
import requests

# 获取session对象
session = requests.session()

# 请求验证码 让session对象记录cookies信息
url_verify = "http://demo6.tp-shop.cn/index.php?m=Home&c=User&a=verify&r=0.2316697196238724"
session.get(url_verify)

# 请求登录
url_login = "http://demo6.tp-shop.cn/Home/User/index.html"
data = {"username":"15376546286",
        "password":"123123",
        "verify_code":8888}
r = session.post(url=url_login, data=data)

# 查看登录是否成功
print(r.json())
# 查询我的订单
url_order = "http://demo6.tp-shop.cn/Home/Order/order_list.html"
r = session.get(url_order)
print(r.text)