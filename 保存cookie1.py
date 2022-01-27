# 导入Selenium的webdriver类
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

'''
options = webdriver.FirefoxOptions()
prefs = {'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)
'''

# 设置变量url，用于浏览器访问
url = 'https://account.cnblogs.com/signin?returnUrl=https:%2F%2Fwww.cnblogs.com%2F'
# 将webdriver类实例化，将浏览器设定为Google Chrome
# 参数executable_path是设置chromedriver的路径
#path = 'E:\\Python\\chromedriver.exe'
driver = webdriver.Firefox()#Chrome(executable_path=path)
# 打开浏览器并访问网址
driver.get(url)



driver.find_element_by_id('mat-input-0').send_keys('657672704@qq.com')
driver.find_element_by_id('mat-input-1').send_keys('111111zxc')

#driver.find_element_by_id('mat-input-1').send_keys(Keys.ENTER)

#driver.find_element_by_class_('mat-focus-indicator').click()

#if (elem.GetAttribute("class").ToString() == "mat-button-wrapper"):
#    elem.InvokeMember("click")
driver.find_element_by_xpath("/html/body/app-root/app-sign-in-layout/div/div/app-sign-in/app-content-container/div/div/div/form/div/button/span[1]").click()

time.sleep(20)


'''

time.sleep(5)
# 添加Cookies
driver.add_cookie({'name': 'Login_User', 'value': 'PassWord'})



# 获取全部Cookies
all_cookies = driver.get_cookies()
print('全部的Cookies为：', all_cookies)



# 获取name为Login_User的Cookie内容
one_cookie = driver.get_cookie('Login_User')
print('单个的Cookie为：', one_cookie)


'''

cookies = driver.get_cookies()
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookies))
f1.close()
