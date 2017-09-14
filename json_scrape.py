# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:56:57 2017

@author: eakin
"""

import requests
import json
numJumpShotsAttempt = 0.0
numJumpShotsMade = 0.0
percJumpShotMade = 0.0

my_wm_username = 'jesnyder'
search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

shots = response.json()
for i in shots:
    if i['ACTION_TYPE'] == 'Jump Shot' and i['EVENT_TYPE'] == 'Made Shot':
        numJumpShotsMade += 1
    if i['ACTION_TYPE'] == 'Jump Shot':
        numJumpShotsAttempt += 1

percJumpShotMade = numJumpShotsMade/numJumpShotsAttempt

            
print my_wm_username
print numJumpShotsAttempt
print numJumpShotsMade
print percJumpShotMade