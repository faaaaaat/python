from urllib import request

def getHtml(url):
    page = request.urlopen(url).read()
    page = page.decode('utf-8')
    return page