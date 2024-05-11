# !/usr/bin/env python3
"""
scrap_amazon.py

This module is used for scraping data from Amazon.

Description:
This module uses the requests and BeautifulSoup libraries to send HTTP requests to Amazon's website and parse the HTML response. It extracts
specific data from the page, such as product details.
"""

import requests
from bs4 import BeautifulSoup

# url = 'https://shopee.com.my/cart/'
url = 'https://www.amazon.com/CeraVe-Moisturizing-Cream-Daily-Moisturizer/dp/B00TTD9BRC?ref_=ast_sto_dp&th=1&psc=1'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), 'html.parser')
print(soup2, "\n\n\n\n\n\n\n\n")
title = soup2.find(_class='AuhAvM')
t2itle = soup2.find('section')
t3itle = soup2.find(id='productTitle')
print(t3itle)
