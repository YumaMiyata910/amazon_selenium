# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.co.jp/')
time.sleep(5)
search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys('Python')
search_box.submit()
time.sleep(5)
driver.quit()