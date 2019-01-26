# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver

# emailとpasswordを.envファイルから取得
AMAZON_EMAIL = os.environ.get('AMAZON_EMAIL')
AMAZON_PASSWORD = os.environ.get('AMAZON_PASSWORD')

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

driver.get('https://www.amazon.co.jp/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=jpflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_signin&switch_account=')
time.sleep(2)

# ログインページにてログイン
email = driver.find_element_by_id("ap_email")
email.send_keys(AMAZON_EMAIL)
password = driver.find_element_by_id("ap_password")
password.send_keys(AMAZON_PASSWORD)
submit_button = driver.find_element_by_id("signInSubmit")
submit_button.click()

time.sleep(2)

# 検索
search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys('Python')
search_box.submit()

time.sleep(5)
driver.quit()