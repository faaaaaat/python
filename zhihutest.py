#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mybase
import re

url = 'http://www.ebd.frank.eyebuy.direct/eyeglasses'
html = mybase.get_url_content(url)
ulInfo = re.compile('<ul class="products-list">.*?<li.*?>(.*?)</li></ul>', re.S)
strlist = re.findall(ulInfo, html)

# liInfo = re.compile('', re.S)
# liIn = re.findall(liInfo, strlist)
print(strlist[0])


# write_info('ebd.txt', strlist)