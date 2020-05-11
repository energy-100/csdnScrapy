import time
from selenium.webdriver.common.action_chains import ActionChains
import sys
# for i in range(20):
#     time.sleep(1)
#     print("****************",end="\r")
#     sys.stdout.flush()
#     time.sleep(1)
#     # sys.stdout.flush()
#     print("********",end="\r")
#     time.sleep(1)
#     sys.stdout.flush()
#     print(str(i*10**(20-i)),end="\r")
#     sys.stdout.flush()
#
# def test():
#     print("\raaaaaaaaaaaaaaa",end = '',flush = True)
#     print("\r***",end = '',flush = True)
#
# test()
# coding: utf-8
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--auto-open-devtools-for-tabs");
chrome_options.add_argument("user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")
client = webdriver.Chrome(chrome_options=chrome_options)
# 如果没有把chromedriver加入到PATH中,就需要指明路径 executable_path='/home/chromedriver'

client.get("https://passport.csdn.net/login?code=public")
print(client.find_element)
time.sleep(5)
    # 封装登录参数
# elem_user = client.find_element_by_id("username")
# elem_user.send_keys("你的用户名")
# elem_pwd = client.find_element_by_id("password")
# elem_pwd.send_keys("你的密码")
# 点击登录按钮

# 获取编辑框的内容
# elem_text = client.find_element_by_xpath("//p[@class='col-xs-12 col-sm-12 control-col-pos col-pr-no col-pl-no']")

# client.find_element_by_xpath("//input[@placeholder='手机号/邮箱/用户名']").send_keys("energy_百分百")
client.find_element_by_link_text("账号密码登录").click()
time.sleep(1)
client.find_element_by_xpath("//input[@placeholder='手机号/邮箱/用户名']").send_keys("18342355667")
client.find_element_by_xpath('//input[@placeholder="密码"]').send_keys("lch19941124")
time.sleep(1)
client.find_element_by_xpath("//button[@class='btn btn-primary']").click()
time.sleep(1)
sizeDict=client.get_window_size()
button=client.find_element_by_class_name("nc_iconfont.btn_slide")
action = ActionChains(client)
action.click_and_hold(button).perform()
action.reset_actions()
action.move_by_offset(280, 0).release().perform()
# action.click_and_hold()
time.sleep(20)
# 关闭谷歌浏览器

# client.get("https://blog.csdn.net/lch551218/article/details/103805042")

content = client.page_source
# client.close()
print(content)
# client.quit()
