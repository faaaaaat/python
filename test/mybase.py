#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import re
import gzip

# 获取网页内容
def get_url_content(url):
    # response = requests.get(url)
    # return requests.get(url).content
    page = request.urlopen(url).read()
    page = page.decode('utf-8')
    return page
# 写入文件
def write_info(file, content):
    f = open(file, 'wt', encoding= 'utf-8')
    f.write(content)
    f.close()
# 标签替换
def replaceTab(x):
    # removeSpace = re.compile(r'[\\t\\r\\n]')
    removeSpace = re.compile('[\\t|\\n]')
    x = re.sub(removeSpace, "", x)
    # replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # # #把段落开头换为\n加空两格
    # replacePara = re.compile('<p.*?>')
    # # #将换行符或双换行符替换为\n
    # replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    # removeNbsp = re.compile('&nbsp;')
    # removeExtraTag = re.compile('<.*?>')
    # x = re.sub(removeExtraTag, "", x)
    # x = re.sub(replaceLine,"",x)
    # x = re.sub(replacePara,"",x)
    # x = re.sub(replaceBR,"",x)
    # x = re.sub(removeNbsp, "", x)
    # removeNbsp = re.compile(' ')
    # x = re.sub(removeNbsp, "", x)
    # strip()将前后多余内容删除
    return x.strip()
#解压缩函数
def ungzip(data):
    try:
        # print("正在解压缩...")
        data = gzip.decompress(data)
        # print("解压完毕...")
    except:
        pass
        # print("未经压缩，无需解压...")
    return data

# print(1)
# url = 'http://www.ebd.frank.eyebuy.direct/eyeglasses'
# print(2)
# html = get_url_content(url)
# print(3)
# ulInfo = re.compile('<ul class="products-list">.*?<li.*?>(.*?)</li></ul>', re.S)
# print(4)
# strlist = re.findall(ulInfo, html)
# print(5)

# # liInfo = re.compile('', re.S)
# # liIn = re.findall(liInfo, strlist)
# print(strlist[0])