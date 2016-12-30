import requests
import re
import mybase

cs_url  = 'https://github.com/login'
cs_user = 'zjf580@163.com'
cs_psw  = 'zheng940221'
my_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
sss     = requests.Session()
r       = sss.get(cs_url, headers = my_headers)
content = mybase.ungzip(r.content).decode('utf-8');
pattern = re.compile('<input name="authenticity_token" type="hidden" value="(.*?)" />', re.S)
result  = re.findall(pattern, content)
token   = result[0]
my_data = {
    'commit' : 'Sign in',
    'utf8' : '%E2%9C%93',
    'authenticity_token' : token,
    'login' : cs_user,
    'password' : cs_psw
}
cs_url  = 'https://github.com/session'
r       = sss.post(cs_url, headers = my_headers, data = my_data)
print(r.url, r.status_code, r.history)

r       = sss.get('https://github.com', headers = my_headers)
content = mybase.ungzip(r.content).decode('utf-8');
f = open('github.html', 'wt', encoding= 'utf-8')
f.write(content)
f.close()


