"""

悟空浏览器自用版
搜索 done/excitation_ad/ 抓该接口的url(...done/excitation_ad/?后的url)、cookie 、argus、ladon
cookies格式 wk = "url#cookie#argus#ladon"
cron: */30 * * * *
new Env('悟空浏览器');

"""
import requests,secrets,time,hashlib,string,random,json,os,sys
import datetime
from lib2to3.pygram import python_grammar_no_print_and_exec_statement
import os
import time
import random
import base64
import requests
import hashlib
import uuid
import json

now = str(round(time.time()*1000))
kami=""
cookies=os.getenv("wk")
ua = "com.cat.readall/11950 (Linux; U; Android 10; zh_CN_#Hans; OXF-AN00; Build/HUAWEIOXF-AN00; Cronet/TTNetVersion:5a18c8d3 2022-07-19 QuicVersion:12a1d5c5 2022-06-27)"



class DY:
    def __init__(self, cookie):
        self.url = cookie.split("#")[0]
        self.cookie = cookie.split("#")[1]
        self.argus = cookie.split("#")[2]
        self.ladon = cookie.split("#")[3]
        

    def run(self):
            
                 jbsl = self.user()
                 jb1 = jbsl
                 print(f"========开始进行今日签到========")
                 point_ss , point_s = self.sign()
                 print(f"签到奖励金币--{point_s}")
                 print(f"签到奖励金币--{point_ss}")
                 ttt = random.randint(25,35)
                 print(f"签到广告奖励金币--休息{ttt}秒")
                 time.sleep(ttt)    
                 pointgg , pointggg = self.task_box(4019)
                 print(f"签到广告奖励金币--{pointgg}")
                 print(f"签到广告奖励金币--{pointggg}")
                 time.sleep(20) 
                 ttt = random.randint(25,35)
                 print(f"签到广告奖励2金币--休息{ttt}秒")
                 time.sleep(ttt)    
                 pointgg , pointggg = self.task_box(4107)
                 print(f"签到广告奖励2金币--{pointgg}")
                 print(f"签到广告奖励2金币--{pointggg}")
                 time.sleep(20) 
                 print(f"========开始进行吃饭补贴========")
                 self.eat_coin()
                 print(f"========开始进行走路赚钱========")
                 pointgg , pointggg = self.task_box(4014)
                 print(f"走路赚金币--{pointgg}")
                 print(f"走路赚金币--{pointggg}")
                 print(f"========开始看广告赚金币========")
                 pointgg , pointggg = self.task_box(4006)
                 print(f"看广告赚金币--{pointgg}")
                 print(f"看广告赚金币--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"看广告2赚金币--休息{ttt}秒")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(4018)
                 print(f"看广告2赚金币--{pointgg}")
                 print(f"看广告2赚金币--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"看广告3赚金币--休息{ttt}秒")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(3012)
                 print(f"看广告3赚金币--{pointgg}")
                 print(f"看广告3赚金币--{pointggg}")
                 print(f"========开始开宝箱赚金币========")
                 self.treasure_box()
                 pointgg , pointggg = self.task_box(4108)
                 print(f"开宝箱广告金币--{pointgg}")
                 print(f"开宝箱广告金币--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"开宝箱连续广告金币--休息{ttt}秒")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(4010)
                 print(f"开宝箱连续广告金币--{pointgg}")
                 print(f"开宝箱连续广告金币--{pointggg}")
                 ttt = random.randint(25,35)
                 print(f"开宝箱连续广告2金币--休息{ttt}秒")
                 time.sleep(ttt) 
                 pointgg , pointggg = self.task_box(4010)
                 print(f"开宝箱连续广告2金币--{pointgg}")
                 print(f"开宝箱连续广告2金币--{pointggg}")
                 time.sleep(20)

                 print(f"========开始账号查资产========")
            
                 jbsl = self.user()
                 jb2 = jbsl
                 jbzg = jb2 - jb1
                 print(f"========开始计算总收益========")
                 print(f"本次运行脚本共获得金币--{jbzg}")
                 
            
   
           
             
    
    def kami(self):
        url = f"https://api2.2cccc.cc/apiv3/card_login&card={kami}&software=jrttkmo&center_id=17898"
        response = requests.request("GET", url=url)
        kamican = response.json().get('code')
        if kamican == "1":
               kamicans = response.json().get('data').get('less_time')
        else:
            kamicans = response.json().get('msg')
        return kamicans , kamican
    
    def kamidu(self,):
        url = f"https://api2.2cccc.cc/apiv3/config&client_type=card&client_content={kami}&type=read&center_id=17898" 
        response = requests.request("GET", url=url)
        if response.json().get('code') == "1":
               if response.json().get('data').get('config')  == "":
                   kamijqm = "检测到你是头次使用本脚本，即将获取机器码上传登记"
                   kamijqmyz = "检测到你是头次使用本脚本，即将获取机器码上传登记"
               else:
                   kamijqm = "机器码获取成功！"
                   kamijqmyz = response.json().get('data').get('config')
               return kamijqm , kamijqmyz
        else:
            kamijqm = "获取失败！"
            kamijqmyz = "获取失败！"
        return kamijqm , kamijqmyz
    
    def kamiwrite(self,md55):
        url = f"https://api2.2cccc.cc/apiv3/config&client_type=card&client_content={kami}&type=write&value={md55}&center_id=17898" 
        response = requests.request("GET", url=url)
        if response.json().get('code') == "1":
            kamijqmm = "登记成功！"
            return kamijqmm
        else:
            kamijqmm = "未知错误！"
            return kamijqmm

    def get_mac_address(self):
      mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
      print("获取机器码成功！")
      return ":".join([mac[e:e+2] for e in range(0,11,2)])


    def user(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/sj/v1/income/page_data?_request_from=web&{self.url}"
        headers = {
            'User-Agent': ua,
            'x-argus': self.argus,
            'x-ladon': self.ladon,
            'Cookie': self.cookie,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("err_no") == 0:
                jbjj = response_json.get('data').get('score_balance') / 33000
                jbj = round(jbjj, 2)
                print(f"今日金币：{response_json.get('data').get('today_score_amount')}金币 现金：{jbj} 元")
                jbsl = response_json.get('data').get('score_balance')
            else:
                print(f"获取用户信息出错{response_json}")
                jbsl = 0
        else:
            print("用户数据过期或者错误")
            jbsl = 0
        return jbsl
    
    def sign(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/news/v1/sign_in/done_task?{self.url}"
        payload = '{}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': 'com.ss.android.article.news/9360 (Linux; U; Android 13; zh_CN; V2055A; Build/TP1A.220624.014; Cronet/TTNetVersion:85102f3e 2023-06-05 QuicVersion:4ad3af5d 2023-05-09)',
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_s = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                point_ss = response.json().get('data').get('reward_amount')
                return point_s , point_ss
            else:
                point_ss = "已经上限了"
                return point_s  , point_ss
            
    def eat_coin(self):
        current_hour = time.localtime().tm_hour
        if (5 <= current_hour <= 9) or (11 <= current_hour <= 14) or (17 <= current_hour <= 20) or (21 <= current_hour <= 24):
            url = f"https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/eat/done?{self.url}"
            body = "{}"
            headers = {
                'User-Agent': ua,
                'x-argus': self.argus,
                'x-ladon': self.ladon,
                'Cookie': self.cookie,
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Connection': 'keep-alive'
            }
            response = requests.post(url, headers=headers, data=body)
            if response.status_code == 200:
                response_json = response.json()
                if response_json.get("err_no") == 0:
                    score_amount = response_json.get('data').get('score_amount')
                    pointgg , pointggg = self.task_box(4011)
                    print(f"吃饭赚钱广告金币--{pointgg}")
                    print(f"吃饭赚钱广告金币--{pointggg}")
                    return True
                else:
                    print(f"[吃饭赚钱]失败：该时间段已领取")
                    return True
            else:
                print(f"请求失败")
            return False
        else:
            print(f"[吃饭赚钱]失败：不在时间段内")
        return False            

            
        
            
    def task_box(self,id):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = {"amount":691,"weight":0,"task_id":id,"is_post_login":False,"ad_from":"coin","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":False,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}
        payload = json.dumps(payload)
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_ssp = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                point_sp = response.json().get('data').get('reward_amount')
                return point_ssp , point_sp
            else:
                point_sp = "已经上限了"
                return point_ssp  , point_sp   

    def treasure_box(self):
        url = f"https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/treasure_box/detail?{self.url}"
        headers = {
            'User-Agent': ua,
            'x-argus': self.argus,
            'x-ladon': self.ladon,
            'Cookie': self.cookie,
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("err_no") == 0 and response_json.get('data').get('left_seconds') != 0:
                print(f"[开启宝箱]失败：还差{response_json.get('data').get('left_seconds')}秒")
                return True
            else:
                url = f"https://api5-normal-lf.toutiaoapi.com/luckycat/gip/v1/daily/treasure_box/done?{self.url}"
                body = "{\"auto_open\":false}"
                headers = {
                    'User-Agent': ua,
                    'x-argus': self.argus,
                    'x-ladon': self.ladon,
                    'Cookie': self.cookie,
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
                }
                response = requests.post(url, headers=headers, data=body)
                if response.status_code == 200:
                    response_json = response.json()
                    print(f"[开启宝箱]获得金币: {response_json.get('data').get('reward_amount')}")
                    return True
                else:
                    print(f"请求失败")
                    return False
        else:
            print(f"请求失败")
        return False


    def xs_sign(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/novel_sdk/v1/task/done/sign_in?{self.url}"
        payload = '{}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        pointxss = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                pointxxss = response.json().get('data').get('amount')
                return pointxss , pointxxss
            else:
                pointxxss = "已经上限了"
                return pointxss , pointxxss  

    def eat(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/news/v1/eat/done_eat?_request_from=web&{self.url}"
        payload = '{}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_cf = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                point_cff = response.json().get('data').get('score_amount')
                return point_cf , point_cff
            else:
                point_cff = "已经上限了"
                return point_cf  , point_cff  
            

            
    def get_step(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":190,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent':ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        pointstep = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                pointstepp = response.json().get('data').get('reward_amount')
                return pointstep , pointstepp
            else:
                pointstepp = "已经上限了"
                return pointstep , pointstepp




    def eat_sp(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":181,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_cfs = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                point_cffs = response.json().get('data').get('reward_amount')
                return point_cfs , point_cffs
            else:
                point_cffs = "已经上限了"
                return point_cfs  , point_cffs  
            
    def read(self):
        url = f"https://api5-normal-hl.toutiaoapi.com/luckycat/news/v1/activity/done_whole_scene_task?{self.url}"
        payload = '{"group_id": "","scene_key": "IndexTabFeed","is_golden_egg": false}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point_read = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                point_readd = response.json().get('data').get('score_amount')
                return point_readd , point_read
            else:
                point_readd = "已经上限了"
                return point_readd , point_read
            
    def kgg(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":210,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent':ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        pointgg = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_tips") == "成功":
                pointggg = response.json().get('data').get('reward_amount')
                return pointgg , pointggg
            else:
                pointggg = "已经上限了"
                return pointgg , pointggg 
             
    def open_box(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = '{"amount":691,"weight":0,"task_id":188,"is_post_login":false,"ad_from":"task","score_source":0,"content":"","ad_id":2,"ad_rit":"2","score_amount":691,"task_key":"excitation_ad\/","extra":{"task_name":"","track_id":"","stage_score_amount":[],"task_id":""},"image_url_light":"","image_url_button":"","ad_alias_position":"task","fixed":false,"image_url_coin":"","coin_count":691,"params_for_special":"luckydog_sdk","static_settings_version":50,"dynamic_settings_version":50,"poll_settings_version":0}'
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
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
            if response.json().get("err_tips") == "成功":
                point = response.json().get('data').get('reward_amount')
                return point2 , point
            else:
                point = "已经上限了"
                return point2 , point
        
    def open_boxlx(self):
        url = f"https://api5-normal-lq.toutiaoapi.com/luckycat/news/v1/task/done/excitation_ad/?{self.url}"
        payload = "{\"task_id\":225,\"exci_extra\":{\"cid\":1770200687669342,\"req_id\":\"20230701160644C93FF92F37A3A1714A5C\",\"rit\":80047},\"extra\":{\"stage_score_amount\":[],\"track_id\":\"\",\"draw_score_amount\":null,\"draw_track_id\":null,\"task_id\":\"\",\"task_name\":\"\",\"enable_fuzzy_amount\":false,\"custom_id\":null}}"
        headers = {
        'Host': 'api5-normal-lq.toutiaoapi.com',
        'x-ss-req-ticket': now,
        'x-vc-bdturing-sdk-version': '3.5.0.cn',
        'sdk-version': '2',
        'passport-sdk-version': '40452',
        'x-tt-request-tag': 'n=0;s=-1;p=0',
        'x-tt-store-region': 'cn-hn',
        'x-tt-store-region-src': 'uid',
        'x-ss-dp': '13',
        'user-agent': ua,
        'x-argus': self.argus,
        'x-ladon': self.ladon,
        'Cookie': self.cookie,
        'content-type': 'application/json',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }
        response = requests.request("POST", url=url, headers=headers, data=payload)
        point4 = response.json().get('err_tips')
        if response.status_code == 200:
            if response.json().get("err_no") == 0:
                point3 = response.json().get('data').get('reward_amount')
                return point4,point3
            else:
                point3 = "已经上限了"
                return point4,point3

    

if __name__ == "__main__":
    cookies = cookies.split("@")
    print(f"【悟空浏览器】共检测到{len(cookies)}个账号")
    print(f"==========================================")
    print(f"悟空浏览器")
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