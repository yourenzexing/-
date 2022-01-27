# coding=utf-8
import time
import requests
from urllib.request import urlopen,Request
from selenium import webdriver
from selenium.webdriver.common.by import By



 
driver = webdriver.Firefox() #打开Chrome
#dirver.maxmize_window() #最大化浏览器窗口
driver.implicitly_wait(8) #设置隐式时间等待


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


'''
 
driver.get("https://www.baidu.com") # 输入百度地址
driver.find_element_by_xpath("//*[@id='kw']").send_keys("csdn")  # 搜索框输入Selenium
driver.find_element_by_xpath("//*[@id='su']").click() # 点击百度一下按钮
'''

f=open('1.txt','r')
str=f.read()
#print(str)
str_list=str.split('\n')
str_list=set(str_list)

for eachone in str_list:
 
    # 导入time模块，等待2秒
 
    time.sleep(2)


    driver.get("https://music.liuzhijin.cn/") # 输入百度地址
    driver.find_element_by_xpath("//*[@id='j-input']").send_keys(eachone)  # 搜索框输入Selenium
    driver.find_element_by_xpath("//*[@id='j-submit']").click() # 点击百度一下按钮
    time.sleep(2)
    #new_url=driver.find_element_by_xpath('//*[@id="j-src-btn"]').click()#.get_attribute('href')
    url=driver.find_element_by_xpath('//*[@id="j-src-btn"]').get_attribute('href')
    if url != None:
        
        if len(url)>0:
            print(url)

            r=requests.get(url,headers=headers)
            with open("g:\\tmp\\"+eachone+'.mp3','wb') as f:
                f.write(r.content)
                f.close

            driver.find_element_by_xpath("//*[@id='j-back']").click()
        else:
            print('bbbbb')
            #driver.find_element_by_xpath("//*[@id='j-back']").click()
            #driver.find_element(by=By.xpath,value="//*[@id='j-back']").click()
            driver.find_element(by=By.XPATH, value='//*[@id="j-back"]').click()
    else:
        print('aaaa')









'''

# 这里通过元素XPath表达式来确定该元素显示在结果列表，从而判断Selenium官网这个链接显示在结果列表。
# 这里采用了相对元素定位方法/../
# 通过selenium方法is_displayed() 来判断我们的目标元素是否在页面显示。<br>
driver.find_element_by_xpath("//div/h3/a[text()='官方']//../a/em[text()='Selenium']").is_displayed()
driver.quit()
'''
