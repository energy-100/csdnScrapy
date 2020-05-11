
import requests
'''代理ip'''
proxies = {
    "http": "http://202.121.96.33:8086",
    "http": "http://58.253.154.179:9999",
    "http": "http://163.204.243.51:9999",
    "http": "http://183.166.20.179:9999",
    "http": "http://183.166.20.179:9999",

    # "https": "https://221.228.17.172:8181",

}

proxies2 =["http://202.121.96.33:8086",
    "http://58.253.154.179:9999",
    "http://163.204.243.51:9999",
    "http://183.166.20.179:9999",
    "http://183.166.20.179:9999",]

'''请求头'''
headers = {
    "Connection": "Close",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    # "Cookie": "BIDUPSID=10FA6916F18B54FF38D559EADD614CF7; PSTM=1559717595; HMACCOUNT=1A654E98409FD986; BDUSS=NQUWFOU2piQmRvUjZ-alQyWHFFMGhYQlJWUGlzNm95Z2J5SXNySnhVbFBaUmhlRUFBQUFBJCQAAAAAAAAAAAEAAADZUV0hv7S6o7XE0MTH6TE5OTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE~Y8F1P2PBdZn; MCITY=-%3A; BAIDUID=8FE77A473BC7AD385A938DB0BD9CD39F:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=CFAOJeC62wIBEoJuuOfyUIOrkEpgL5bTH6aoRvqxCFQrpapl1wQ1EG0PHU8g0KAbpgWlogKKBmOTHn_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tb4D_CIyfII3fP36q46EbnL_hxJb54cQ24o2WbCQQbIW8pcNLTDKhtAlqq5X-RQ9MIQPal7-2hPhOl7C-lO1j4_eyHQHhRJeb66K2lRPfP3Jfh5jDh3o3jksD-Rt5foRHR5y0hvc0J6cShnkBUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2b6QhDGAJtTkqJJPsBTrL2nTVHtoG-tT8Mt_Hqxby26nm3e69aJ5nJDobOqoHhU6h5f4E2JoAWbjW36RM2I5tQpP-HJ7-5RQWLUKuKl3KbPADbaCDKl0MLpnlbb0xyUQDK--ihMnMBMnGamOnanr73fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5v-eH3P; delPer=0; PSINO=1; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1586651518|; H_PS_PSSID=1434_31170_21107_30826_31186_30905_31270_30824_31085_31163_31195",
    # "Host": "hm.baidu.com",
    # "Referer": "https://blog.csdn.net/dreamzuora/article/details/89931656",
    }

currentPageUrl="https://blog.csdn.net/lch551218/article/details/104067710"
currentPag_html = requests.get(currentPageUrl, headers=headers, proxies=proxies)  # 访问该网站
main_html =currentPag_html.text
print(main_html)
