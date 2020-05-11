import random
import time
from pyquery import PyQuery as pq
import requests
from bs4 import BeautifulSoup
import math
import os
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import operator
# import urwid
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')


'''请求头'''
headers = {
    "Connection": "Close",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    # "Cookie": "BIDUPSID=10FA6916F18B54FF38D559EADD614CF7; PSTM=1559717595; HMACCOUNT=1A654E98409FD986; BDUSS=NQUWFOU2piQmRvUjZ-alQyWHFFMGhYQlJWUGlzNm95Z2J5SXNySnhVbFBaUmhlRUFBQUFBJCQAAAAAAAAAAAEAAADZUV0hv7S6o7XE0MTH6TE5OTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE~Y8F1P2PBdZn; MCITY=-%3A; BAIDUID=8FE77A473BC7AD385A938DB0BD9CD39F:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=CFAOJeC62wIBEoJuuOfyUIOrkEpgL5bTH6aoRvqxCFQrpapl1wQ1EG0PHU8g0KAbpgWlogKKBmOTHn_F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tb4D_CIyfII3fP36q46EbnL_hxJb54cQ24o2WbCQQbIW8pcNLTDKhtAlqq5X-RQ9MIQPal7-2hPhOl7C-lO1j4_eyHQHhRJeb66K2lRPfP3Jfh5jDh3o3jksD-Rt5foRHR5y0hvc0J6cShnkBUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2b6QhDGAJtTkqJJPsBTrL2nTVHtoG-tT8Mt_Hqxby26nm3e69aJ5nJDobOqoHhU6h5f4E2JoAWbjW36RM2I5tQpP-HJ7-5RQWLUKuKl3KbPADbaCDKl0MLpnlbb0xyUQDK--ihMnMBMnGamOnanr73fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5v-eH3P; delPer=0; PSINO=1; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1586651518|; H_PS_PSSID=1434_31170_21107_30826_31186_30905_31270_30824_31085_31163_31195",
    # "Host": "hm.baidu.com",
    # "Referer": "https://blog.csdn.net/dreamzuora/article/details/89931656",


}

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

# s=requests.session()
# s.keep_alive = False

class artobject():
    def __init__(self):
        self.id=""
        self.title=""
        self.url=""
        self.views=-1
        self.comments=-1
        self.data=""
        self.data=""
        self.ontop=False
        self.pageat=-1
        self.pageurl=""

# 爬取csdn类
class ScrapyCSDNArticle:
    ''' class for csdn'''

    def __init__(self, blogname):
        self.titles=dict()
        self.articlenumsParPage=-1
        self.articlenums=-1
        self.pages=-1
        self.printlen=0
        self.articaldatas=[]
        self.blogname=blogname
        csdn_url = 'https://blog.csdn.net/'
        self.blogurl = csdn_url + self.blogname  # 拼接字符串成需要爬取的主页url
        self.res=requests.Session()


    def getArticalNums(self):
        # main_response=""
        # try:
        main_response = requests.get(self.blogurl+"/article/list/1", headers=headers)
        # main_response = requests.get(self.blogurl+"/article/list/1", headers=headers, proxies=proxies)
        # print(main_response.status_code)
        # print(main_response.cookies)
        # except Exception as errorinf:
        #     print(errorinf)
        # 判断是否成功获取 (根据状态码来判断)
        if main_response.status_code == 200:
            print('获取成功')
            self.main_html = main_response.text
            main_doc = pq(self.main_html)
            mainpage_str = main_doc.text()  # 页面信息去除标签信息
            origin_position = mainpage_str.index('码龄')  # 找到原创的位置
            # print("************",mainpage_str[mainpage_str.index('76')-5:mainpage_str.index('76')+5])
            end_position = mainpage_str.index('原创', origin_position + 1)  # 最终的位置,即原创底下是数字多少篇博文
            self.blog_nums = ''
            # 获取写的博客数目
            # print(mainpage_str[end_position-4:end_position])
            for num in range(2, 10):
                # 判断为空格 则跳出循环
                if mainpage_str[end_position - num]== "\n":
                # if mainpage_str[end_position + num].isspace() == True:
                    break
                self.blog_nums = mainpage_str[end_position - num]+self.blog_nums
            self.articlenums = int(self.blog_nums)  # 获得当前博客文章数量
            print('文章总数：'+str(self.articlenums))
        else:
            print('访问网站失败:')
        return self.articlenums  # 返回博文数量

    def getarticleinf(self):
        if self.articlenums == 0 or self.articlenums == -1:
            print('检测到0篇文章，请先执行getOriginalArticalNums函数获取文章总数！')
        else:
            main_response = requests.get(self.blogurl, headers=headers, proxies=proxies)
            if main_response.status_code == 200:

                # 获取文章总数
                # self.getArticalNums()

                # 获取总页数
                main_html = main_response.text
                soup = BeautifulSoup(main_html, 'html.parser')
                self.articlenumsParPage = len(soup.find_all('p', class_="content"))
                if self.articlenumsParPage == self.articlenums:
                    self.pages = 1
                else:
                    self.pages = math.ceil(self.articlenums / self.articlenumsParPage)
                print("博客页数为：" + str(self.pages))

                # 获取文章url
                for page in range(1, self.pages + 1):
                    currentPageUrl = self.blogurl + '/article/list/%d' % page + '?t=1&'  # 拼接字符串
                    currentPag_html = requests.get(currentPageUrl, headers=headers, proxies=proxies)  # 访问该网站
                    # 先判断是否成功访问
                    if currentPag_html.status_code == 200:
                        currentPag_text = currentPag_html.text
                        soup = BeautifulSoup(currentPag_text, 'html.parser')
                        for index, articalTag in enumerate(soup.find_all(class_='article-item-box csdn-tracking-statistics')):
                            articaldata=artobject()
                            articaldata.title = articalTag.h4.a.select("span")[0].next_sibling
                            articaldata.url = articalTag.find('a')['href']
                            articaldata.id = articaldata.url.split("/")[-1]
                            articaldata.views = int(articalTag.select('.read-num')[0].get_text())
                            articaldata.comments = int(articalTag.select('.read-num')[1].get_text())
                            articaldata.data = articalTag.select('.date')[0].string.strip()
                            articaldata.ontop = True if len(articalTag.select('.icon.settop'))>0 else False
                            articaldata.pageat = page
                            articaldata.pageurl = currentPageUrl
                            # print(articaldata.data)
                            self.articaldatas.append(articaldata)
                self.articaldatas.sort(key=lambda x:x.views,reverse=True)
            else:
                print("访问博客主页失败！")
        for data in self.articaldatas:
            print(data.id,data.views,data.comments,data.ontop,data.pageat)



    def changeTime(self,allTime):
        day = 24 * 60 * 60
        hour = 60 * 60
        min = 60
        if allTime < 60:
            return "%d 秒" % math.ceil(allTime)
        elif allTime > day:
            days = divmod(allTime, day)
            return "%d 天, %s" % (int(days[0]), self.changeTime(days[1]))
        elif allTime > hour:
            hours = divmod(allTime, hour)
            return '%d 小时, %s' % (int(hours[0]), self.changeTime(hours[1]))
        else:
            mins = divmod(allTime, min)
            return "%d 分, %d 秒" % (int(mins[0]), math.ceil(mins[1]))




    def ScrapyArticals(self,repeat,sleeptime):
        timestart=time.perf_counter()
        timeend=time.perf_counter()+sleeptime
        if self.pages == -1:
            print('请先获取文章总数！')
            return False
        else:
            viewcount=0
            runtimestr=timestart
            speed=0
            for count in range(repeat):
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                # chrome_options.add_argument("--proxy-server="+random.choice(proxies2))
                chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")
                client = webdriver.Chrome(chrome_options=chrome_options)
                endindex = random.randint(1, len(self.articaldatas))
                for index in range(endindex):
                    data=self.articaldatas[index]
                    try:

                        # currentPag_html = requests.get(data.url, headers=headers, proxies=proxies)  # 访问该网站


                        # chrome_options = webdriver.ChromeOptions()
                        # chrome_options.add_argument('--headless')
                        # chrome_options.add_argument('--disable-gpu')
                        # # chrome_options.add_argument("--proxy-server="+random.choice(proxies2))
                        # chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")
                        # client = webdriver.Chrome(chrome_options=chrome_options)
                        client.get(data.url)
                        # client.quit()
                        # currentPag_html = requests.get(data.url, headers=headers, proxies=proxies)  # 访问该网站
                        # 先判断是否成功访问
                        if True:
                        # if currentPag_html.status_code == 200:
                            viewcount += 1
                            nowtime = time.perf_counter() - timestart
                            runtimestr = self.changeTime(nowtime)
                            speed=round(viewcount/nowtime*60*60)
                            pstr = "\r文章" + data.id + "(" + str(index+1) + "/" + str(
                                endindex) + ")访问成功,已访问次数:" + str(viewcount) + " 访问速度:" + str(
                                speed) + "次/h 已运行时间：" + runtimestr
                            print("\r" + " " * self.printlen, end=" ", flush=True)
                            print(pstr, end=" ", flush=True)
                            self.printlen = len(pstr) * 2
                            # self.printlen = get_width(ord(pstr))
                    except Exception as errorinf:
                        # print(errorinf)
                        pstr = "\r文章" + data.id + "(" + str(index+1) + "/" + str(
                                endindex) + ")访问失败\n"
                        print("\r" + " " * self.printlen, end=" ", flush=True)
                        print(pstr, end=" ", flush=True)
                        self.printlen = len(pstr) * 2

                pstr = "\r暂停中...已访问次数:" + str(viewcount) + " 访问速度:" + str(speed) + "次/h 已运行时间：" + runtimestr
                print("\r" + " " * self.printlen, end=" ", flush=True)
                print(pstr, end="", flush=True)
                self.printlen = len(pstr) * 2
                # self.printlen=get_width(ord(pstr))
                sleeptime=random.randint(6,10)
                time.sleep(sleeptime)
            client.quit()
            print("访问结束......")



# 如何调用该类
# logname=input("请输入博客名称：")
# ScrapyCSDNA = ScrapyCSDNArticle(logname)  # 初始化类 参数为博客名
ScrapyCSDNA = ScrapyCSDNArticle('lch551218')  # 初始化类 参数为博客名
ScrapyCSDNA.getArticalNums()
ScrapyCSDNA.getarticleinf()
# ScrapyCSDNA.getPageNums()
ScrapyCSDNA.ScrapyArticals(10000,10)
# for i in range(1, 600):
#     ScrapyCSDNA.ScrapyArticals()
#     time.sleep(10)  # 给它休息时间 还是怕被封号的