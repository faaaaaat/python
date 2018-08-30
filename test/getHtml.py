from urllib import request

def getHtml(url, headers):
    if len(headers):
        url = request.Request(url=url, headers=headers)
    page = request.urlopen(url).read()
    page = page.decode('GBK')
    return page