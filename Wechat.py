#  -*- coding: utf-8 -*-
#  @IDE :  PyCharm
#  @Time : 2017/11/21 10:10
#  @Author ： Daisy
#  @ProjectNmae : Wechat

'''
What about:使用图灵接口，连接微信，图灵机器人聊天
当登陆微信之后，只需好友发信息，就可以实现与图灵机器人聊天

'''
from wxpy import *


# 实例化，并登录微信
bot = Bot(cache_path=True)
# 查找到要使用机器人来聊天的好友
my_friend = ensure_one(bot.search(u'何勺叶'))
# 调用图灵机器人API
tuling = Tuling(api_key='f51f9df3c3fc4fa4a38de5dc043f558d')
# tuling = Tuling(api_key='4a0488cdce684468b95591a641f0971d')
# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
embed()

'''

# 实例化，并登录微信''
bot = Bot(cache_path=True)
# 调用图灵机器人API
tuling = Tuling(api_key='f51f9df3c3fc4fa4a38de5dc043f558d')

# tuling = Tuling(api_key='4a0488cdce684468b95591a641f0971d')

@bot.register()
def reply_my_friend(msg):
    tuling.do_reply(msg)


embed()
'''
