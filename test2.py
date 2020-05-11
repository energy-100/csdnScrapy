# -*- coding: UTF-8 -*-
import urllib
from urllib import request
from http import cookiejar
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # 设置保存cookie的文件的文件名,相对路径,也就是同级目录下
    filename = 'Cookies'
    # 创建MozillaCookieJar实例对象
    cookie = cookiejar.MozillaCookieJar(filename)
    # 从文件中读取cookie内容到变量
    # cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)

    loginUrl = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

    # 登陆前准备：获取lt和exection

    response = opener.open(loginUrl)

    # 获取表单隐藏的登录信息
    soup = BeautifulSoup(response.read(), 'lxml')
    for input in soup.form.find_all("input"):
        if input.get("name") == "lt":
            lt = input.get("value")
        if input.get("name") == "execution":
            execution = input.get("value")

    # post信息

    postdata = {
        "username": "18342355667",
        "password": "lch19941124",
        "lt": lt,
        "execution": execution,
        "_eventId": "submit"
    }

    postdata = urllib.parse.urlencode(postdata).encode('utf-8')

    # 此用opener的open方法打开网页
    opener.addheaders = [("User-Agent",
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36")]
    result = opener.open(loginUrl, postdata)

    # 保存cookie

    cookie.save(ignore_discard=True, ignore_expires=True)

    # 登陆后我们随意跳转到博客获取内容
    url = "http://my.csdn.net/my/mycsdn"
    response = opener.open(url)
    html = response.read().decode('utf-8')
    f = open('csdn.html', 'w')
    f.write(html)
    f.close()
    print('ok')