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

# 导包  unittest  requests
import requests
import unittest

# 新建测试类 -->unittest.TestCase
class TestLogin(unittest.TestCase):

        # setup
        def setUp(self):
                # 获取session对象
                self.session = requests.session()
                # 登录url
                self.url_login = "http://demo6.tp-shop.cn/Home/User/index.html"
                # 验证码url
                self.url_verify = "http://demo6.tp-shop.cn/index.php?m=Home&c=User&a=verify&r=0.2316697196238724"
        # tearDown
        def tearDown(self):
                # 关闭session
                self.session.close()
        # 登录成功
        def test_login_success(self):
                # 请求验证码 -->获取cookies
                self.session.get(self.url_verify)
                # 请求登录
                data = {"username": "15376546286",
                        "password": "123123",
                        "verify_code": 8888}
                r = self.session.post(self.url_login, data=data)
                try:
                        # 断言
                        self.assertEqual("登录成功", r.json()['mag'])
                except AssertionError as e:
                        print(e)
        # 登录失败  账号不存在
        def test_username_not_exist(self):
                # 请求验证码 -->获取cookies
                self.session.get(self.url_verify)
                # 请求登录
                data = {"username": "153765462861",
                        "password": "123123",
                        "verify_code": 8888}
                r = self.session.post(self.url_login, data=data)
                try:
                        # 断言
                        self.assertEqual("账号不存在", r.json()['mag'])
                except AssertionError as e:
                        print(e)
        # 登录失败  密码错误
        def test_password_error(self):
                self.session.get(self.url_verify)
                data = {"username": "153765462861",
                        "password": "123123",
                        "verify_code": 8888}
                r = self.session.post(self.url_login, data=data)
                try:
                        self.assertEqual("密码错误", r.json()["mag"])
                except AssertionError as e:
                        print(e)

if __name__ == '__main__':
    unittest.main()