# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 14:35:59 2017

@author: eakin
"""

import requests
from bs4 import BeautifulSoup as bsoup
sublist_state = []
sublist_county = []
sublist_percent = []
my_result_list = []    
my_wm_username = 'jesnyder'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content

parsed_html = bsoup(response, "lxml")
target_rows = parsed_html.find_all('tr')  # will find one row of data
#target_rows = parsed_html.find_all('tr', attrs={'id' : re.compile('^pgl_advanced.')})  # uses Regex.  Will find all rows of data

all_games = []
for row in target_rows:
    new_row = []
    for x in row.find_all('td'):
        new_row.append(x.text)
        
    my_result_list.append(new_row)
    

print my_wm_username
print len(my_result_list)
print my_result_list