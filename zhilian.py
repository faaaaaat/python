# -*-encoding:utf-8-*-

import urllib.parse
import re
import urllib.request
import mybase

def getHtml(url, headers):
    req=urllib.request.Request(url, headers=headers)

    page = urllib.request.urlopen(req).read()
    page = mybase.ungzip(page)
    page = page.decode('utf-8')

    return page


# 获取工作信息网址连接
def getJobSite(city="上海", keywords="php", pastday=1,maxpage=91,sf=0,st=99999):
    jobUrl = []
    for i in range(1, maxpage):#最大90页
        arg = dict(jl=city, kw=keywords, p=i, pd=pastday, isadv=1, sf=sf, st=st)

        page_data = urllib.parse.urlencode(arg)
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + page_data
        #根据网站报头信息设置headers
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
            'Connection':'Keep-Alive',
            'If-Modified-Since':0,
            'Host':'sou.zhaopin.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        }
        page = getHtml(url, headers)
        pagePartten = re.compile('onkeypress="zlapply.searchjob.enter2Page\(this,event,([0-9]+)\)')
        if re.findall(pagePartten, page) != []:
            pagenum = int(re.findall(pagePartten, page)[0])

            if pagenum > i:
                jobPartten = re.compile('par="ssidkey=y&amp;ss=201&amp;ff=03" href="(.*?)" target="_blank" onclick="submitLog')
                jobList = re.findall(jobPartten, page)
                if jobList != []:
                    jobUrl += jobList
    return set(jobUrl)


# 具体工作网页信息
def getJobInfo(joblist,filename):
    global items
    #根据网站报头信息设置headers
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'Keep-Alive',
        'If-Modified-Since':0,
        'Host':'jobs.zhaopin.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    try:
        items = list(set(joblist))
    except:
        pass
    j = 1
    total = len(items)
    # 写入txt文件
    f = open(filename, 'wt', encoding= 'utf-8')
    try:
        for item in items:
            html = getHtml(item, headers)

            f.write(item + '\t')
            # 获取职位及公司名称
            comPartten = re.compile('<div class="inner-left fl">.*?<h1>(.*?)</h1>.*?<h2>.*?target="_blank">(.*?)</a></h2>', re.S)
            companyInfo = re.findall(comPartten, html)  # 列表件套元组形如[(a,b)]
            try:
                f.write(companyInfo[0][0] + '\t' + replaceTab(companyInfo[0][1]) + '\t')
                # 获取工作相关信息
                jobPartten1 = re.compile('<ul class="terminal-ul clearfix">(.*?)</ul>', re.S)
                jobInfo1 = re.findall(jobPartten1, html)

                jobPartten2 = re.compile('<li>.*?<strong>(.*?)</strong></li>')
                jobInfo2 = re.findall(jobPartten2, jobInfo1[0])  # 列表长度为8
                for i in jobInfo2:
                    f.write(replaceTab(i) + "\t")

                # 工作职能表述
                jobPartten3 = re.compile('<div class="terminalpage-main clearfix">(.*?)<button .*?</button>', re.S)
                jobInfo3 = re.findall(jobPartten3, html)
                f.write(replaceTab(jobInfo3[0]) + '\n')
                print("writing the " + str(j) + u"th information. tatol:" + str(total))
                j = j + 1
            except:
                f.write('\n')
    except:
        f.write('\n')
    f.close()


# 标签替换
def replaceTab(x):
    removeSpace = re.compile('[\t\r\n\f\v]')
    # replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # # #把段落开头换为\n加空两格
    # replacePara = re.compile('<p.*?>')
    # # #将换行符或双换行符替换为\n
    # replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeNbsp = re.compile('&nbsp;')
    removeExtraTag = re.compile('<.*?>')
    # x = re.sub(replaceLine,"",x)
    # x = re.sub(replacePara,"",x)
    # x = re.sub(replaceBR,"",x)
    x = re.sub(removeExtraTag, "", x)
    x = re.sub(removeNbsp, "", x)
    x = re.sub(removeSpace, "", x)
    # strip()将前后多余内容删除
    return x.strip()

print("开始采集------------")
city = '上海'
keyWord = 'php'
#城市，关键词，最近几天，抓取几页数据（默认全部）
items = getJobSite(city, keyWord, 7, 2, 15000,20000)
filename = city + keyWord + '.txt'

getJobInfo(items,filename)
print("采集结束------------")


