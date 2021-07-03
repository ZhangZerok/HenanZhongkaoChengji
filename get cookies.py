from selenium.webdriver import Edge
import time
import json
driver = Edge("C:\MicrosoftWebDriver\MicrosoftWebDriver")
driver.get('http://gzgl.jyt.henan.gov.cn/zk/')
time.sleep(80)
with open('cookies.txt','w') as f:
     f.write(json.dumps(driver.get_cookies()))
driver.close