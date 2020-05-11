
import time
from pyquery import PyQuery as pq
import requests
from bs4 import BeautifulSoup
import math
import os
import sys
from selenium.webdriver.common.action_chains import ActionChains
# import urwid
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')


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
# s=requests.session()
# s.keep_alive = False


# 爬取csdn类
class ScrapyCSDNArticle:
    ''' class for csdn'''

    def __init__(self, blogname):
        self.titles=dict()
        self.articlenumsParPage=-1
        self.articlenums=-1
        self.pages=-1
        self.printlen=0
        self.blogname=blogname
        csdn_url = 'https://blog.csdn.net/'
        self.blogurl = csdn_url + self.blogname  # 拼接字符串成需要爬取的主页url
        self.res=requests.Session()

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

    def getArticalNums(self):
        # main_response=""
        try:
            main_response = requests.get(self.blogurl,headers=headers,)
            # main_response = requests.get(self.blogurl, headers=headers, proxies=proxies)
        except Exception as errorinf:
            print(errorinf)
        # 判断是否成功获取 (根据状态码来判断)
        if main_response.status_code == 200:
            print('获取成功')
            self.main_html = main_response.text
            main_doc = pq(self.main_html)
            mainpage_str = main_doc.text()  # 页面信息去除标签信息
            print(mainpage_str)
            origin_position = mainpage_str.index('TA的个人主页')  # 找到原创的位置
            # print("************",mainpage_str[mainpage_str.index('76')-5:mainpage_str.index('76')+5])
            end_position = mainpage_str.index('原创', origin_position + 1)  # 最终的位置,即原创底下是数字多少篇博文
            self.blog_nums = ''
            # 获取写的博客数目
            for num in range(3, 10):
                # 判断为空格 则跳出循环
                if mainpage_str[end_position + num].isspace() == True:
                    break
                self.blog_nums += mainpage_str[end_position + num]
            self.articlenums = int(self.blog_nums)  # 获得当前博客文章数量
            print('文章总数：'+str(self.articlenums))
        else:
            print('访问网站失败:'+errorinf)
        return self.articlenums  # 返回博文数量

    def getPageNums(self):
        if self.articlenums == 0 or self.articlenums==-1:
            print('检测到0篇文章，请先执行getOriginalArticalNums函数获取文章总数！')
        else:
            main_response=requests.get(self.blogurl,headers=headers, proxies=proxies)
            if main_response.status_code == 200:
                main_html = main_response.text
                soup = BeautifulSoup(main_html, 'html.parser')
                self.articlenumsParPage=len(soup.find_all('p', class_="content"))
                if self.articlenumsParPage==self.articlenums:
                    self.pages=1
                else:
                    self.pages=math.ceil(self.articlenums/self.articlenumsParPage)
                print("博客页数为："+str(self.pages))
            else:
                print("访问博客主页失败！")
        return self.pages

    def ScrapyArticals(self,repeat,sleeptime):
        timestart=time.perf_counter()
        timeend=time.perf_counter()+sleeptime
        if self.pages == -1:
            print('请先获取文章总数！')
            return False
        else:
            viewcount=0
            runtimestr=timestart
            for count in range(repeat):
                for page in range(1, self.pages + 1):
                    currentPageUrl = self.blogurl + '/article/list/%d' % page + '?t=1&'  # 拼接字符串
                    currentPag_html = requests.get(currentPageUrl,headers=headers, proxies=proxies)  # 访问该网站
                    # 先判断是否成功访问
                    if currentPag_html.status_code == 200:
                        currentPag_text = currentPag_html.text
                        soup = BeautifulSoup(currentPag_text, 'html.parser')
                        for index,articalTag in enumerate(soup.find_all(class_='article-item-box csdn-tracking-statistics')):
                            articaltitle=articalTag.h4.a.select("span")[0].next_sibling
                            articalUrl=articalTag.find('a')['href']
                            try:
                                status=requests.get(articalUrl,headers=headers, proxies=proxies)  # 进行访问
                                if status.status_code == 200:
                                    viewcount+=1
                                    nowtime=time.perf_counter()-timestart
                                    runtimestr=self.changeTime(nowtime)
                                    pstr="\r文章"+articalUrl.split("/")[-1]+"("+str((page-1)*self.articlenumsParPage+index+1)+"/"+str(self.articlenums)+")访问成功,已访问次数:"+str(viewcount)+" 访问速度:"+str(round((count)*self.articlenums/(timeend-timestart)*60*60,2))+"次/h 已运行时间："+runtimestr
                                    print("\r"+" "*self.printlen,end=" ",flush=True)
                                    print(pstr,end=" ",flush=True)
                                    self.printlen = len(pstr)*2
                                    # self.printlen = get_width(ord(pstr))
                            except Exception as errorinf:
                                # print(errorinf)
                                pstr="\r文章" + articalUrl.split("/")[-1] + "(" + str(
                                    (page - 1) * self.articlenumsParPage + index + 1) + "/" + str(
                                    self.articlenums) + ")访问失败\n"
                                print("\r" + " " * self.printlen, end=" ", flush=True)
                                print(pstr, end=" ", flush=True)
                                self.printlen = len(pstr) * 2
                                # print("\n文章" + articalUrl.split("/")[-1] + "(" + str(
                                #     (page - 1) * self.articlenumsParPage + index + 1) + "/" + str(
                                #     self.articlenums) + ")访问失败\n")
                                # print("文章" + articalUrl.split("/")[-1] + "(" + str(
                                #     (page - 1) * self.articlenumsParPage + index + 1) + "/" + str(
                                #     self.articlenums) + ")访问失败"+str(errorinf))
                pstr="\r暂停中...已访问次数:"+str(viewcount)+" 访问速度:"+str(round((count)*self.articlenums/(timeend-timestart)*60*60))+"次/h 已运行时间："+runtimestr
                print("\r"+" "* self.printlen,end=" ",flush=True)
                print(pstr,end="",flush=True)
                self.printlen = len(pstr)*2
                # self.printlen=get_width(ord(pstr))
                time.sleep(10)
                timeend=time.perf_counter()
        print('访问结束')



# 如何调用该类
# logname=input("请输入博客名称：")
# ScrapyCSDNA = ScrapyCSDNArticle(logname)  # 初始化类 参数为博客名
# ScrapyCSDNA = ScrapyCSDNArticle('lch551218')  # 初始化类 参数为博客名
ScrapyCSDNA = ScrapyCSDNArticle('love666666shen')  # 初始化类 参数为博客名
ScrapyCSDNA.getArticalNums()
ScrapyCSDNA.getPageNums()
ScrapyCSDNA.ScrapyArticals(10000,10)
# for i in range(1, 600):
#     ScrapyCSDNA.ScrapyArticals()
#     time.sleep(10)  # 给它休息时间 还是怕被封号的