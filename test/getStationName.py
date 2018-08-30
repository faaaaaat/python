#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import mybase
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

def getStationName(station):
    #根据网站报头信息设置headers
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'Keep-Alive',
        'If-Modified-Since':0,
        'Host':'kyfw.12306.cn',
        'Referer':'https://kyfw.12306.cn/otn/lcxxcx/init',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

    # url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2017-01-24&from_station=SHH&to_station=AQH"
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8992" 
    req=urllib.request.Request(url, headers=headers)
    res=urllib.request.urlopen(req)

    # #读取知乎首页内容，获得_xsrf
    data = res.read()
    data = mybase.ungzip(data)
    data = data.decode('utf-8')


    jobPartten = re.compile(station + '\|(.*?)\|', re.S)
    jobList = re.findall(jobPartten, data)
    return jobList[0]
    # f = open('stationname.txt', 'wt', encoding= 'utf-8')
    # f.write(data)
    # f.close()
