import requests
import re
import mybase
import base64
import json
import rsa
import binascii

cs_url  = 'https://weibo.com'
username = '13955424735'
password  = 'zheng940221'


WBCLIENT = 'ssologin.js(v1.4.5)'
session     = requests.Session()


my_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
def encrypt_passwd(passwd, pubkey, servertime, nonce):
    key = rsa.PublicKey(int(pubkey, 16), int('10001', 16))
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(passwd)
    passwd = rsa.encrypt(message.encode('utf-8'), key)
    return binascii.b2a_hex(passwd)


resp = session.get(
    'http://login.sina.com.cn/sso/prelogin.php?'
    'entry=sso&callback=sinaSSOController.preloginCallBack&'
    'su=%s&rsakt=mod&client=%s' %
    (base64.b64encode(username.encode('utf-8')), WBCLIENT)
)
pattern = re.compile(r'[^{]+({.+?})', re.S)
result  = re.findall(pattern, resp.text)
result = json.loads(result[0])
data = {
    'entry': 'weibo',
    'gateway': 1,
    'from': '',
    'savestate': 7,
    'userticket': 1,
    'ssosimplelogin': 1,
    'su': base64.b64encode(requests.utils.quote(username).encode('utf-8')),
    'service': 'miniblog',
    'servertime': result['servertime'],
    'nonce': result['nonce'],
    'vsnf': 1,
    'vsnval': '',
    'pwencode': 'rsa2',
    'sp': encrypt_passwd(password, result['pubkey'],
                         result['servertime'], result['nonce']),
    'rsakv' : result['rsakv'],
    'encoding': 'UTF-8',
    'prelt': '115',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.si'
           'naSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}
resp = session.post(
    'http://login.sina.com.cn/sso/login.php?client=%s' % WBCLIENT,
    data=data
)
pattern = re.compile(r'replace\([\"\']([^\'\"]+)[\"\']', re.S)
result  = re.findall(pattern, resp.text)
resp = session.get(result[0])

i = 1
a = 0
url = 'http://weibo.com/p/1005051086233511/follow?relate=fans&page=' + str(i)

#     resp = session.get(getfansurl, headers = my_headers)
# getfansurl = 'http://weibo.com/p/1005051086233511/follow?relate=fans&page=4#Pl_Official_HisRelation__62'

while a == 0:
    resp = session.get(url, headers = my_headers)
    pattern = re.compile(r'刘大大熊', re.S)
    result  = re.findall(pattern, resp.text)
    if result != []:
        f = open('weibo.html', 'wt', encoding= 'utf-8')
        f.write(result[0])
        f.close()
        a = 1
    print(i)
    i = i + 1
# resp = mybase.replaceTab(resp.text)
# print(resp)
# f = open('weibo.html', 'wt', encoding= 'utf-8')
# f.write(resp.text)
# f.close()


# f = open('weibo.html', 'wt', encoding= 'utf-8')
# f.write(result[0])
# f.close()
# if result == []:
#     print(11111)

# r       = sss.get(cs_url, headers = my_headers)
# content = mybase.ungzip(r.content).decode('utf-8');
# pattern = re.compile('<input name="authenticity_token" type="hidden" value="(.*?)" />', re.S)
# result  = re.findall(pattern, content)
# token   = result[0]
# my_data = {
#     'commit' : 'Sign in',
#     'utf8' : '%E2%9C%93',
#     'authenticity_token' : token,
#     'login' : cs_user,
#     'password' : cs_psw
# }
# cs_url  = 'https://github.com/session'
# r       = sss.post(cs_url, headers = my_headers, data = my_data)
# print(r.url, r.status_code, r.history)

# r       = sss.get('https://github.com', headers = my_headers)
# content = mybase.ungzip(r.content).decode('utf-8');
# f = open('github.html', 'wt', encoding= 'utf-8')
# f.write(content)
# f.close()


