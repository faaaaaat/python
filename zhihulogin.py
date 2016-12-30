import requests
import re
import mybase
import time
import os.path
try:
    from PIL import Image
except:
    pass


sss     = requests.Session()
sss.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    sss.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

my_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = sss.get(captcha_url, headers=my_headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


# cs_url  = 'https://github.com/login'
cs_user = '13955424735'
cs_psw  = '940221'
# r       = sss.get(cs_url, headers = my_headers)
# content = mybase.ungzip(r.content).decode('utf-8');
# pattern = re.compile('<input name="authenticity_token" type="hidden" value="(.*?)" />', re.S)
# result  = re.findall(pattern, content)
# token   = result[0]
my_data = {
    '_xsrf' : 'Sign in',
    'password' : cs_psw,
    'phone_num' : cs_user,
    'captcha' : get_captcha()
}
cs_url  = 'https://www.zhihu.com/login/phone_num'
r       = sss.post(cs_url, headers = my_headers, data = my_data)
print(r.url, r.status_code, r.history, r.text)
url = 'https://www.zhihu.com/inbox'

r       = sss.get(url, headers = my_headers)
content = mybase.ungzip(r.content).decode('utf-8');
f = open('github.html', 'wt', encoding= 'utf-8')
f.write(content)
f.close()


