from time import sleep
from selenium.webdriver import Edge
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time,datetime
starttime=datetime.datetime(2021,7,2,15,50,0)
while datetime.datetime.now()<starttime:
    time.sleep(1)
    print('稍等，您的成绩正在赶来的路上......')
driver = Edge("C:\MicrosoftWebDriver\MicrosoftWebDriver")
driver.get('http://gzgl.jyt.henan.gov.cn/zk/')
f1 = open('cookies.txt')
cookie = f1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
driver.refresh()
above=driver.find_element_by_link_text('普通高中')
ActionChains(driver).click(above).perform()
element = driver.find_element_by_css_selector('#layui-layer-shade1')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)
up=driver.find_element_by_link_text('中招成绩查询')
ActionChains(driver).click(up).perform()
try:
    picture_url=driver.save_screenshot('.\\chenji.png')
    print("%s ：截图成功！！！" % picture_url)
except BaseException as msg:
    print("%s ：截图失败！！！" % msg)
driver.quit()
