# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

# 検索URL
open_url = "https://item.fril.jp/b877d26b1b96142fdeb54d35e6fbadef"

response = urllib.request.urlopen(open_url)
html = response.read()

# print(html)

soup = BeautifulSoup(html, "html.parser")

item_names =  soup.find_all("h1")

# 4番目が商品名
"""
count = 1
for item_name in item_names:
	print(count)
	print()
	print(item_name)
	print("\n")
	count += 1
"""

print(item_names[3])

