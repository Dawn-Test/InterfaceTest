"""
目标：响应对象常用方法
    1.encoding
        1）.获取请求编码
        2）.获取响应编码
    2.headers
        1）.获取响应头信息
案例：
    http：//www.baidu.com
"""

# 导包
import requests

# 调用get 方法
url = "http://www.baidu.com"
r = requests.get(url)

# 查看请求默认编码格式  ISO-8859-1
print(r.encoding)

# 设置响应编码
r.encoding = "utf-8"

# 查看响应内容 text形式
print(r.text)

# 查看响应信息头
# 提示：headers 信息比较重要 （项目工作中一般服务器返回的token/session信息都在headers中）
print(r.headers)