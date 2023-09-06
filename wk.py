"""
悟空浏览器自用版
by 偷CK的六舅哥
无限刷金币
cookies格式 url#cookie#argus#ladon
wkllq_ck = "url#cookie#argus#ladon"
7.3 悟空浏览器刷视频，不黑一天4块左右
暂时未写异常处理,bug提交 https://t.me/jiangyutck
9.6 增加变量提交
"""

import datetime
import os
import time
import random
import base64
import requests
import json


env_name = 'wk' 
cookies = os.getenv(env_name)

ua = ""

num=30 #循环参数

class DY:
    def __init__(self, cookie):
        self.url = cookie.split("#")[0]
        self.cookie = cookie.split("#")[1]
        self.argus = cookie.split("#")[2]
        self.ladon = cookie.split("#")[3]
        

    def run(self):
       jbsl = self.user()
       jb1 = jbsl
       print(f"========开始无限刷金币========")
       for i in range(num):
         tt = random.randint(50,70)
         print(f"开宝箱奖励金币--休息{tt}秒")
         time.sleep(tt)
         i = i +1
         point , point2 = self.open_box()
         print(f"第{i}次开宝箱奖励金币--{point2}")
         print(f"第{i}次开宝箱奖励金币--{point}")
       print(f"========开始账号查资产========")
       jbsl = self.user()
       jb2 = jbsl
       jbzg = jb2 - jb1
       print(f"========开始计算总收益========")
       print(f"本次运行脚本共获得金币--{jbzg}")



    def user(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/sj/v1/income/page_data?_request_from=web&{self.url}"
        headers = {
        'Host': 'api5-normal-hl.toutiaoapi.com',
        'user-agent': 'com.cat.readall/11930 (Linux; U; Android 10; zh_CN_#Hans; SPN-AL00; Build/HUAWEISPN-AL00; Cronet/TTNetVersion:5a18c8d3 2022-07-19 QuicVersion:12a1d5c5 2022-06-27)',
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("GET", url=url, headers=headers)
        
        if response.status_code == 200:
         if response.json().get("err_no") == 0:
            jbjj = response.json().get('data').get('score_balance') / 33000
            jbj = round(jbjj, 2)
            print(f"当前金币：{response.json().get('data').get('score_balance')}金币 现金：{jbj} 元")
            jbsl = response.json().get('data').get('score_balance')
         else:
            print(f"获取用户信息出错{response.json()}")
            jbsl = 0
        else:
         print("用户数据过期或者错误")
         jbsl = 0
        return jbsl

    def open_box(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/gip/v1/cooperate/exciad/done?{self.url}"
        payload = "{\"task_id\":4108,\"exci_extra\":{\"cid\":1572200687669348,\"req_id\":\"20230701160644C93FF92F37A3A1714A5C\",\"rit\":80047},\"extra\":{\"stage_score_amount\":[],\"track_id\":\"\",\"draw_score_amount\":null,\"draw_track_id\":null,\"task_id\":\"\",\"task_name\":\"\",\"enable_fuzzy_amount\":false,\"custom_id\":null}}"
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'user-agent': 'com.cat.readall/11930 (Linux; U; Android 10; zh_CN_#Hans; SPN-AL00; Build/HUAWEISPN-AL00; Cronet/TTNetVersion:5a18c8d3 2022-07-19 QuicVersion:12a1d5c5 2022-06-27)',
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point2 = response.json().get('err_tips')
        if response.status_code == 200:
            point2 = response.json().get('err_tips')
            if response.json().get("err_tips") == "成功":
                point = response.json().get('data').get('reward_amount')
                return point2 , point
            else:
                point = "已经上限了"
                return point2 , point
        


    

if __name__ == "__main__":
    cookies = cookies.split("@")
    print(f"【悟空浏览器】共检测到{len(cookies)}个账号")
    print(f"==========================================")
    print(f"悟空浏览器自用版(小毛)   by:偷CK的六舅哥\n7.3 悟空浏览器刷视频，不黑一天1-2块左右\n暂时未写异常处理，bug提交 https://t.me/jiangyutck")
    i = 1
    for cookie in cookies:
        print(f"========【账号{i}】开始运行脚本========")
        i += 1
        DY(cookie).run()
        
        time.sleep(random.randint(5, 10))
        if i > len(cookies):
            break
        else:
            print("延迟一小会,准备跑下一个账号")
