import time
from pyquery import PyQuery as pq
import requests
from bs4 import BeautifulSoup
import math
import os
import sys
'''请求头'''
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
}

'''代理ip'''
proxies = {
    "http": "http://202.121.96.33:8086",
    "http": "http://58.253.154.179:9999",
    "http": "http://163.204.243.51:9999",
    "http": "http://183.166.20.179:9999",
    "http": "http://183.166.20.179:9999",
    "http": "http://49.86.181.35:9999",

    # "https": "https://221.228.17.172:8181",

}
try:
    main_response=requests.get("https://blog.csdn.net/lch551218",headers=headers, proxies=proxies)
    print(main_response.text)
except Exception as a:
    print(a)