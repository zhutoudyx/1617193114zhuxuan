# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
headers = {'User-agent': 'Mozilla/4.0 (compatible: MSIE 5.5: Windows NT)'}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    # print response.read()
    html = response.read().decode('utf-8')
    
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason



content_pattern = re.compile('<div class="content">.*?<span>(.*?)</span>', re.S)
content_items = re.findall(content_pattern, html)
for item in content_items:
    print item

    
smile_count_pattern = re.compile('<span class="stats-vote">.*?<i class="number">(.*?)</i>', re.S)
smile_items = re.findall(smile_count_pattern, html)

for item in smile_items:
    print item


comments_count_pattern = re.compile('<span class="stats-comments">.*?<i class="number">(.*?)</i>', re.S)
comments_items = re.findall(comments_count_pattern, html)

for item in comments_items:
    print item
