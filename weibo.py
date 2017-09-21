import json
import time
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import http.cookiejar as cookielib
agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}
driver=webdriver.Chrome("G:\Python3.5\selenium\webdriver\chromedriver.exe")
# driver=webdriver.PhantomJS('G:\Python3.5\Scripts\phantomjs.exe')
driver.get('http://passport.weibo.cn/signin/login')
driver.set_page_load_timeout(3000)
time.sleep(5)
while True:
    try:
        driver.find_element_by_id('loginName').send_keys('departureszy@sina.cn')
        driver.find_element_by_id('loginPassword').send_keys('521241')
        driver.find_element_by_id('loginPassword').send_keys(Keys.ENTER)
        break
    except ElementNotVisibleException:
        print ("ElementNotVisibleException")

# driver.find_element_by_id('loginName').send_keys('departureszy@sina.cn')
# driver.find_element_by_id('loginPassword').send_keys('521241')
# driver.find_element_by_id('loginPassword').send_keys(Keys.ENTER)
time.sleep(3)
print("Login Success")
# 获取cookie并通过json模块将dict转化成str
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('weibocookie', 'w') as f:
    f.write(jsonCookies)

# driver.delete_all_cookies()
# # 读取登录时存储到本地的cookie
# with open('cookies.json', 'r', encoding='utf-8') as f:
#     listCookies = json.loads(f.read())
# for cookie in listCookies:
#     driver.add_cookie({
#         'domain': '.xxxx.com',  # 此处xxx.com前，需要带点
#         'name': cookie['name'],
#         'value': cookie['value'],
#         'path': '/',
#         'expires': None
#     })
print(jsonCookies)

cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
cookiestr = ';'.join(item for item in cookie)
print (cookiestr)


