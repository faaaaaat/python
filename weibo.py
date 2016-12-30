#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
  
from weibopy.auth import OAuthHandler  
from weibopy.api import API  
import ConfigParser  
import time  
  
  
MAX_PIC_NUM = 5  
SLEEP_TIME_LONG = 30  
  
  
def press_sina_weibo():  
    ''''' 
    调用新浪微博Open Api实现通过命令行写博文，功能有待完善 
    author: socrates 
    date:2012-02-06 
    新浪微博：@没耳朵的羊 
    '''  
    sina_weibo_config = ConfigParser.ConfigParser()  
    #读取appkey相关配置文件  
    try:  
        sina_weibo_config.readfp(open('sina_weibo_config.ini'))  
    except ConfigParser.Error:  
        print 'read sina_weibo_config.ini failed.'  
      
    #获取需要的信息  
    consumer_key = sina_weibo_config.get("userinfo","CONSUMER_KEY")  
    consumer_secret =sina_weibo_config.get("userinfo","CONSUMER_SECRET")  
    token = sina_weibo_config.get("userinfo","TOKEN")  
    token_sercet = sina_weibo_config.get("userinfo","TOKEN_SECRET")  
  
  
    #调用新浪微博OpenApi(python版)  
    auth = OAuthHandler(consumer_key, consumer_secret)  
    auth.setToken(token, token_sercet)  
    api = API(auth)  
    return api;  
  
  
    #通过命令行输入要发布的内容  
#    weibo_content = raw_input('Please input content:')  
#    status = api.update_status(status=weibo_content)  
#    print "Press sina weibo successful, content is: %s" % status.text  
#    iNum = 0  
#    while True:  
#        #上传图片，名称和内容如果重复，open api会检查，内容采用了取当前时间的机制  
#        #图片名称从0-5循环遍历  
#        status = api.upload(str(iNum)+ '.jpg', time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))  
#        time.sleep(SLEEP_TIME_LONG)  
#      
#        if iNum == MAX_PIC_NUM:  
#            iNum = 0  
#        else:  
#            iNum += 1  
  
  
def get_friends(api, user_id):    
    ''''' 
    Function:获取关注的用户列表 
    Input：api 
           user_id:指定用户的ID 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-04-14 
    '''     
    print 'friends list: '  
    total_friends = 0  
    next_cursor = -1  
    while next_cursor != 0:  
        timeline = api.friends(user_id,'','','',next_cursor)  
        if isinstance(timeline, tuple):  
                next_cursor = timeline[1]  
                total_friends += len(timeline[0])  
                for line in timeline[0]:  
                    fid = line.__getattribute__("id")  
                    name = line.__getattribute__("screen_name")  
                    text = "friends---"+ str(fid) +":"+ name  
                    text = text.encode("gbk")  
                    print text  
        else:  
            next_cursor = 0  
            total_friends += len(timeline)  
            for line in timeline:  
                fid = line.__getattribute__("id")  
                name = line.__getattribute__("screen_name")  
                text = "friends---"+ str(fid) +":"+ name  
                text = text.encode("gbk")  
                print text  
                  
    print 'Total friends: %d' % total_friends            
  
  
def get_followers(api, user_id):    
    ''''' 
    Function:获取用户的粉丝 
    Input：api 
           user_id:指定用户的ID 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-04-14 
    '''     
    print 'followers list: '  
    total_friends = 0  
    next_cursor = -1  
    while next_cursor != 0:  
        timeline = api.followers(user_id,'','','',next_cursor)  
        if isinstance(timeline, tuple):  
                next_cursor = timeline[1]  
                total_friends += len(timeline[0])  
                for line in timeline[0]:  
                    fid = line.__getattribute__("id")  
                    name = line.__getattribute__("screen_name")  
                    text = "followers---"+ str(fid) +":"+ name  
                    text = text.encode("gbk")  
                    print text  
        else:  
            next_cursor = 0  
            total_friends += len(timeline)  
            for line in timeline:  
                fid = line.__getattribute__("id")  
                name = line.__getattribute__("screen_name")  
                text = "followers---"+ str(fid) +":"+ name  
                text = text.encode("gbk")  
                print text  
                  
    print 'Total followers: %d' % total_friends        
def main():  
    #获取关注列表  
    get_friends(press_sina_weibo(), 2601091753)    
      
    #获取粉丝  
    # get_followers(press_sina_weibo(), 2601091753)       
                       
if __name__ == '__main__':  
    main()  