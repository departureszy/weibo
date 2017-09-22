import json
import re

import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import html

# driver=webdriver.Chrome("G:\Python3.5\selenium\webdriver\chromedriver.exe")
driver=webdriver.PhantomJS()
driver.get('http://passport.weibo.cn/signin/login')
driver.set_page_load_timeout(3000)
time.sleep(5)
while True:
    try:
        driver.find_element_by_id('loginName').send_keys('username')
        driver.find_element_by_id('loginPassword').send_keys('password')
        driver.find_element_by_id('loginPassword').send_keys(Keys.ENTER)
        break
    except ElementNotVisibleException:
        print ("ElementNotVisibleException")
print("Login success")
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('weibocookie', 'w') as f:
    f.write(jsonCookies)
# driver.delete_all_cookies()
time.sleep(3)
# 读取登录时存储到本地的cookie
# with open('weibocookie', 'r', encoding='utf-8') as f:
#     listCookies = json.loads(f.read())
# for cookie in listCookies:
#     driver.add_cookie({
#         'domain': cookie['domain'],
#         'name': cookie['name'],
#         'value': cookie['value'],
#         'path': '/',
#         'expires': None
#     })
# print("Login with cookie success")
driver.get('https://m.weibo.cn/u/3914043390')#访问微博主页
driver.maximize_window()
time.sleep(4)

# # 获取所有微博
# driver.find_elements_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/nav/div/div/div/ul/li[2]').clear()
# time.sleep(2)
#
# page=1
# while page<150:
#     driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
#     driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
#     driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
#     page=page+1
# time.sleep(3)
#
# weibocontentssoup=BeautifulSoup(driver.page_source,'html.parser')
# contentsclass=weibocontentssoup.findAll('div',{'class':'card-main'})
# driver.quit()
# for data in contentsclass:
#     date=re.findall('<span class="time">(.*?)</span>', str(data))
#     phone=re.findall('<span class="from">(.*?)</span>', str(data))
#     re.findall('<div class="weibo-text">(.*?)</div>', str(data))
#     weiboog=re.findall('<div class="weibo-text">(.*?)</div>', str(data))
#     weiborp=re.findall('"()"', str(data))
#     print(date)
#     print(phone)
#     print(weiboog)
#     print(weiborp)
#     # with open('weibo-all.txt', 'a',encoding = 'utf-8') as f:
#     #     f.write(date+' '+phone)
#
#
# print('文件写入完成')



# #获取所有关注人的信息 并写入文件
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[1]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div/ul/li[2]').click()
# time.sleep(1)
#
# page=1
# while page<100:
#     driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
#     driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
#     driver.find_element_by_xpath('/html/body').send_keys(Keys.PAGE_DOWN)
#     page=page+1
# time.sleep(3)
#
# followdetailsoup=BeautifulSoup(driver.page_source,'html.parser')
# personclass=followdetailsoup.findAll('div',{'class':'m-text-box'})
# driver.quit()
# for data in personclass:
#     name=re.findall('<span>(.*?)</span>', str(data))
#     info=re.findall('<h4 class="m-text-cu.*?">(.*?)</h4>',str(data))
#     print(name)
#     print(info)
#
#     with open('linaifollow.txt', 'a',encoding = 'utf-8') as f:
#         f.write('昵称：'+name[0]+'\n')
#         if len(info)==1:
#             f.write('签名：'+'(无签名)'+'\n')
#             f.write('' + info[0] + '\n')
#         else:
#             f.write('签名：'+info[0]+'\n')
#             f.write(''+info[1]+'\n')
#
# print('文件写入完成')



# driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/nav/div/div/div/ul/li[2]/span').click() #所有微博

# 发送私信
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div/div[2]').click()
time.sleep(10)
i=0
# driver.refresh()
while i<50:
    driver.find_element_by_xpath('//*[@id="chat-sendmsg-box"]/div[1]/textarea').send_keys('李狗狗')
    # time.sleep(2)
    driver.find_element_by_xpath('//*[@id="chat-sendmsg-box"]/section/div[2]/button').click()
    time.sleep(1)
    i=i+1
driver.quit()
# print(driver.page_source)
