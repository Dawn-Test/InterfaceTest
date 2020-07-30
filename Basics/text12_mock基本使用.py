# 导包（unittest  mock）
import unittest
from unittest import mock

# 未实现的函数
def add(x, y):
    pass

# 新建测试类 继承
class TestAdd(unittest.TestCase):
    pass
    # 新建测试方法
    def test_add(self):

        # 获取mock对象 并设置行为 替换为完成或未实现的对象
        add = mock.Mock(return_value=18)  # return_value 设置行为（返回字符串、数值、对象）
        # 调用未实现的对象
        result = add(10, 20)
        # 断言
        self.assertEqual(result, 30)

if __name__ == '__main__':
    unittest.main()