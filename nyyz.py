"""
能源宇宙 by 压妹蝶----20231210

！！！重要！！！
所有资金盘都不要充值，娱乐就好，年底了，被骗了别找我
所有资金盘都不要充值，娱乐就好，年底了，被骗了别找我
所有资金盘都不要充值，娱乐就好，年底了，被骗了别找我

浏览器打开：https://nyshare.igmdns.com/index.html?inviteCode=14014



变量名 nyyzcookie=手机号#密码，多账号换行

一天一次，看6+6个广告

"""


import os
from urllib.parse import unquote
import time
import random
import base64
import requests
import json
import re
import string  

from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad, unpad  


cookies = os.getenv("nyyzcookie")


def encrypt(key, plaintext):  
    cipher = AES.new(key, AES.MODE_ECB)  
    padded_plaintext = pad(plaintext.encode(), AES.block_size)  
    ciphertext = cipher.encrypt(padded_plaintext)  
    encoded_ciphertext = base64.b64encode(ciphertext)  
    return encoded_ciphertext  


class nyyz:
    def __init__(self, i, cookie):
        self.phone=cookie.split("#")[0]  
        self.password=cookie.split("#")[1]  
        self.token=''       #登录token
        self.appVersion=''     #app版本，很重要
        self.nickname=''     #用户名
        self.userId=''     #用户id
        self.spar=''     #能源晶石
        self.adCount=''   #已看广告数量，总数量为6
        self.nyyzId=''
        self.appAdId=''
        self.lotteryOdd=''

    def run(self):
        self.login()            
        self.userinfo()
        self.adshouye6()
        self.adchoujiang6()
        self.userinfo()
        print('运行结束')
        
            
#用户信息
    def userinfo(self):
        try:
            url = "https://nyapi.igmdns.com/api/user/info"
            json={}
            headers={
                "Accept-Encoding": "identity",
                "Content-Type": "application/json",
                "authorization": self.token,
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Host": "nyapi.igmdns.com",
                "Connection": "Keep-Alive",
                "Content-Length": "2"
            }
            r = requests.post(url,headers=headers,json=json).json()
            if r["code"]==0:
                self.appVersion=r["data"]["appVersion"]     #app版本，很重要
                self.nickname=r["data"]["nickname"]     #用户名
                self.spar=r["data"]["spar"]     #晶石
                self.quota=r["data"]["quota"]   #晶石额度
                self.wallet=r["data"]["wallet"]   #余额
                print(f'【晶石】{self.spar}')
                print(f'【余额】{self.wallet}')
                print(f'【晶石额度】{self.quota}')
                return True
            else:
                print('获取信息失败',r)
                return False
            #print(r)
        except Exception as e:
            print("错误0",e,r)
            return False
            
#看首页6广告
    def adshouye6(self):
        maxLoop=0
        while (self.adCount<6):  #看每日广告
            time1=int(time.time() * 1000)   
            self.adparam(1)#首页6广告
            print('模拟看广告等待45秒')
            time.sleep(45)
            time2=int(time.time() * 1000)   
            self.reward_video(time1,time2)
            self.adcheck()
            time.sleep(2)
            maxLoop+=1
            if maxLoop>6:
                break   #最多循环6次
        self.givereward()   #点击领奖
            
#抽奖6广告
    def adchoujiang6(self):
        maxLoop=0
        while (self.lotteryOdd>0):  #看每日广告抽奖
            time1=int(time.time() * 1000)   
            self.adparam(2)#抽奖6广告
            print('模拟看广告等待45秒')
            time.sleep(45)
            time2=int(time.time() * 1000)   
            self.reward_video(time1,time2)
            self.adcheck()
            self.lottery()
            time.sleep(2)
            maxLoop+=1
            if maxLoop>6:
                break   #最多循环6次
            
#登录获取token
    def login(self):
        try:
            url = "https://nyapi.igmdns.com/api/login"
            json={
                "mobile": self.phone,
                "password": self.password
            }
            headers={
                "Accept-Encoding": "identity",
                "Content-Type": "application/json",
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Host": "nyapi.igmdns.com",
                "Connection": "Keep-Alive",
                "Content-Length": str(len(json))
            }
            r = requests.post(url,headers=headers,json=json).json()
            if r["code"]==0:

                self.token=r["data"]["token"]       #登录token
                self.appVersion=r["data"]["appVersion"]     #app版本，很重要
                self.nickname=r["data"]["nickname"]     #用户名
                self.userId=r["data"]["userId"]     #用户id
                self.spar=r["data"]["spar"]     #能源晶石
                self.adCount=r["data"]["adCount"]   #已看广告数量，总数量为6
                self.lotteryOdd=r["data"]["lotteryOdd"]   #剩余抽奖次数，总数量为6
                print(f'【{self.nickname}】登录成功')
                print(r)
                return True
            else:
                print('登录失败',r)
                exit()
                return False
            #print(r)
        except Exception as e:
            print("错误1",e,r)
            return False
            
            
#获取广告信息
    def adparam(self,type):
        try:
            url = "https://nyapi.igmdns.com/api/ad/param"
            headers={
                "Accept-Encoding": "identity",
                "Content-Type": "application/json",
                "authorization": self.token,
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Host": "nyapi.igmdns.com",
                "Connection": "Keep-Alive",
                "Content-Length": "10"
            }
            json={
                "type": type,
                }
            r = requests.post(url,headers=headers,json=json).json()
            if r["code"]==0:
                self.nyyzId=r["data"]["nyyzId"]
                self.appAdId=r["data"]["appAdId"]
                print(f'获取广告ID成功:{self.nyyzId}')
            else:
                print('获取个人信息失败',r)
        except Exception as e:
            print("错误2",e,r)
            return False
            
#判断看完广告
    def adcheck(self):
        try:
            url = "https://nyapi.igmdns.com/api/ad/check"
            headers={
                "Accept-Encoding": "identity",
                "Content-Type": "application/json",
                "authorization": self.token,
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Host": "nyapi.igmdns.com",
                "Connection": "Keep-Alive",
                "Content-Length": "17"
            }
            json={
                "nyyzId": self.nyyzId,
                }
            r = requests.post(url,headers=headers,json=json).json()
            if r["data"]["check"]==1:
                self.adCount=r["data"]["adCount"]   #已看广告数量，总数量为6
                print(f'看广告成功，已看广告:{r["data"]["adCount"]}')
            else:
                print('看广告失败',r)
        except Exception as e:
            print("错误3",e,r)
            return False
            
#看完广告奖励
    def reward_video(self,time1,time2):
        try:
            key = "155fcf351d81c949"  # 16字节的随机密钥 
            key = key.encode('utf-8')
            str1 = '{"sdk_version":"4.3.0.2","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; zh-CN; Redmi Note 7 MIUI\/V12.5.7.0.QFGCNXM)","network":1,"play_start_ts":'+str(time1)+',"play_end_ts":'+str(time2)+',"user_id":"'+str(self.userId)+'","trans_id":"d91fb147-2ddc-4f58-8d38-a28356a7777a","link_id":"46378b87-02ab-4596-8b1a-a8fcaab4d950","prime_rit":"'+str(self.appAdId)+'","adn_rit":"13515000025","reward_name":"战舰收益领取","reward_amount":3,"media_extra":"'+str(self.nyyzId)+'","adn_name":"ks","ecpm":"6000.0"}'
            url = "https://api-access.pangolin-sdk-toutiao.com/api/ad/union/mediation/reward_video/reward/"
            json={
                "message": ('21d81c949155fcf35'.encode('utf-8')+encrypt(key,str1)).decode('utf-8'),
                "cypher": 2
            }
            headers={
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; zh-CN; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": str(len(json)),
                "Host": "api-access.pangolin-sdk-toutiao.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip"
            }
            r = requests.post(url,headers=headers,json=json).text
            print('看广告完成',r)
        except Exception as e:
            print("错误4",e)
            return False
            
#看完首页6广告领取奖励
    def givereward(self):
        try:
            url = "https://nyapi.igmdns.com/api/machine/give/reward"
            headers={
                "Accept-Encoding": "identity",
                "Content-Type": "application/json",
                "authorization": self.token,
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Host": "nyapi.igmdns.com",
                "Connection": "Keep-Alive",
                "Content-Length": "2"
            }
            json={}
            r = requests.post(url,headers=headers,json=json).json()
            if r["code"]==0:
                self.spar=r["data"]["spar"]     #能源晶石
                print(f'领取奖励【{r["data"]["rewardSpar"]}】能源晶石成功，当前一共有【{rself.spar}】能源晶石')
            else:
                print('领取奖励失败',r)
        except Exception as e:
            print("错误5",e,r)
            return False

#看完抽奖广告抽奖
    def lottery(self):
        try:
            url = "https://nyapi.igmdns.com/api/lottery"
            headers={
                "Accept-Encoding": "identity",
                "Content-Type": "application/json",
                "authorization": self.token,
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.5.7.0.QFGCNXM)",
                "Host": "nyapi.igmdns.com",
                "Connection": "Keep-Alive",
                "Content-Length": "2"
            }
            json={}
            r = requests.post(url,headers=headers,json=json).json()
            if r["code"]==0:
                self.spar=r["data"]["spar"]     #能源晶石
                self.lotteryOdd=r["data"]["lotteryOdd"]     #剩余抽奖次数
                print(f'抽奖成功，还剩【{self.lotteryOdd}】次广告抽奖')
            else:
                print('领取奖励失败',r)
        except Exception as e:
            print("错误6",e,r)
            return False



if __name__ == "__main__":
    cookies = cookies.split("\n")
    print('能源宇宙！！！开始运行')
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
        print(f"\n---开始第{i}个账号---")
        nyyz(i,cookie).run()
        i += 1
        print('等待2秒开始下一个账号')
        time.sleep(2)
