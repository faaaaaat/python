#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import mybase
import ssl
import re
import getStationName

ssl._create_default_https_context = ssl._create_unverified_context


def getYuPiao(time, chufa = 'SHH', daoda = 'AQH',zuoweilx = 'ze_num'):
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
        'X-Requested-With':'XMLHttpRequest',
    }

    url = "https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=" + time + "&from_station=" + chufa + "&to_station=" + daoda 
    req=urllib.request.Request(url, headers=headers)
    res=urllib.request.urlopen(req)

    # #读取知乎首页内容，获得_xsrf
    data = res.read()
    data = mybase.ungzip(data)
    data = data.decode('utf-8')

    jobPartten = re.compile('datas.*?\[(.*?)\]', re.S)
    jobList = re.findall(jobPartten, data)
    if jobList != []:
        #车次需要更换，或者不填车次
        jobPartten = re.compile('\{.*?G7080.*?' + zuoweilx + '":"(.*?)".*?}', re.S)
        jobList = re.findall(jobPartten, jobList[0])
        return jobList
    else:
        jobPartten = re.compile('message":"(.*?)"', re.S)
        jobList = re.findall(jobPartten, data)
        return jobList
    return '查找失败'


    # print(len(jobList))

    # f = open('12306.txt', 'wt', encoding= 'utf-8')
    # f.write(jobList[0])
    # f.close()

print(getYuPiao('2017-01-26', getStationName.getStationName('上海'), getStationName.getStationName('安庆')))
