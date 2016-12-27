# -*-encoding:utf-8-*-

import urllib.parse
import re
from urllib import request

def getHtml(url):
	page = request.urlopen(url).read()
	page = page.decode('utf-8')
	return page


# 获取工作信息网址连接
def getJobSite(city="上海", keywords="php", pastday=1,maxpage=91):
	jobUrl = []
	for i in range(1, maxpage):#最大90页
		arg = dict(jl=city, kw=keywords, p=i, pd=pastday, isadv=0,kt=3)

		page_data = urllib.parse.urlencode(arg)
		url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + page_data
		page = getHtml(url)
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
			html = getHtml(item)

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
