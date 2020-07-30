"""
目标：响应对象常用方法
    1.cookies
        获取响应cookies信息
    2.content
        以字节码形式获取响应信息（图片、视频...多媒体格式）
案例：
    cookies：http：//www.baidu.com
    content：http：//www.baidu.com/img/bd_logo1.png?where=super
"""

# 导包
import requests

# 调用get方法
url = "http://www.baidu.com"
# r = requests.get(url)
# 百度logo
url_img = "http://www.baidu.com/img/bd_logo1.png?where=super"
r = requests.get(url_img)

# 获取响应cookies信息
# print("cookies信息：", r.cookies)

# 通过键名获取响应的cookies值
# print("cookies信息：", r.cookies['BDORZ'])

# 以text文本形式解析图片  -->  乱码
# print(r.text)

# 以字节码形式解析图片
# print(r.content)

# 将图片写入当前目录baidu.png
with open("./baidu.png", "wb")as f:
    f.write(r.content)