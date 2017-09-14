# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 14:19:34 2017

@author: eakin
"""

import requests
from lxml import objectify
from lxml import etree

parameter = 'tavg'
state_id = 44
num_months = 6
end_month = 8
year = '2016'
template_base = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-'
template_base = template_base + 'rankings/download.xml?parameter='
template_add = '%s&'
template_add = template_add + '&state=%s&div=0&month=%s&periods[]=%s&year=%s'
insert_these = (parameter,state_id,end_month,num_months,year)
template_add = template_add % insert_these

response = requests.get(template_base + template_add).content
root = objectify.fromstring(response)
print 'Username: jesnyder'
print 'Value: ',root['data']['value']
print '20th Century Mean: ',root['data']['twentiethCenturyMean']
print 'Low Rank: ',root['data']['lowRank']
print 'High Rank: ',root['data']['highRank']
