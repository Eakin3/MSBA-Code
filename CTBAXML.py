# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 00:26:34 2017

@author: eakin
"""

import requests
from lxml import objectify
from lxml import etree

num_periods = 1
parameter = 'tavg'
state_id = 44
num_months = 6
year = '2016'
template_base = 'http://www.ncdc.noaa.gov/temp-and-precip/climatological-'
template_base = template_base + 'rankings/index.php?periods%5B%5D='
template_add = '%s&'
template_add = template_add + 'parameter=%s&state=%s&div=0&month=%s&'
template_add = template_add +'year=%s#ranks-form'
insert_these = (num_periods, parameter,state_id,num_months,year)
template_add = template_add % insert_these
print template_base + template_add