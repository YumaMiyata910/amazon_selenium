# -*- coding: utf-8 -*-

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.pointmp4.com/en')
time.sleep(5)
search_box = driver.find_element_by_id("search")
search_box.send_keys('https://www.youtube.com/watch?v=8VSO6iYC7L0')
search_box.submit()


time.sleep(5)
# driver.quit()