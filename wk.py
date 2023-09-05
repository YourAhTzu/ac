"""
悟空浏览器自用版
by 偷CK的六舅哥
无限刷金币
cookies格式 url#cookie#argus#ladon
wkllq_ck = "url#cookie#argus#ladon"
7.3 悟空浏览器刷视频，不黑一天4块左右
暂时未写异常处理,bug提交 https://t.me/jiangyutck

"""

import datetime
import os
import time
import random
import base64
import requests
import json


cookies= "scm_build_version=1.0.0.2421&luckydog_base=tq9gZZZxH35Yad86NQ7jebgiTf3D1WN4CmJfJcf65nY8zI3Ewu_Re_OkOoYm2ZaqktP73Ag6-xsc7Wn4BmS3MAwDcshUbabiQeye8p6rS2R50Zib5NSz5HoRHbMVqBo1W325EQ_O3W7BN6bt2wvCCL9VvoilfrIT8frYAITmCIk&luckydog_data=Dpnn4qrHQLcNW1peO73kOPMRXYAQQ-YAF2U1A-njQoJFPhWg4m_fjPSvM9bTplPeCeuM18uBzFHTq7iSFFUAzFhb_YU5X26TZDbKY7FHYdc&luckydog_token=g9GikH_OwQZy4R6G1MKWM-NoGolenyV8sq--rxW6eTXqV5s4GqAeThKg3v4NW74o&luckydog_sdk_version=7.0.0-rc.13-sj1&luckydog_api_version=7.0.0-rc.13-sj1&luckydog_settings_version=51051&device_platform=android&os=android&ssmix=a&_rticket=1693792999269&_rticket=1693792999282&cdid=a8c5eb04-e6e7-4c5e-bdc5-62392efda9e4&channel=44952650j&aid=6589&app_name=gold_browser&version_code=1193&version_name=1.9.3&manifest_version_code=11930&update_version_code=119304&ab_version=3835809%2C4676864%2C5945879%2C6714491%2C6743372%2C6934270%2C6973879%2C7011718%2C7044179%2C5447744%2C5672285%2C3234117%2C3825461%2C4257484%2C4806284%2C5059678%2C5823487%2C6311616%2C6486392%2C6488752%2C6684396%2C6804112%2C6831214%2C6851817%2C6852934%2C6935058%2C6951921%2C7017311%2C7036264%2C7036283%2C7037180%2C7039350%2C7043331%2C7043396%2C6286008&ab_group=94569%2C102756&ab_feature=94563%2C102749&resolution=720*1470&dpi=320&device_type=V2068A&device_brand=vivo&language=zh&os_api=30&os_version=11&access=4g&dq_param=1&plugin=0&pass_through=44952650j&recommend_switch=true&isTTWebView=0&session_id=6a1388e1-5409-4995-9a64-a2d53028e009&host_abi=arm64-v8a&is_db=0&rom_version=originos+1.0_pd2068b_a_1.25.8&iid=3767400127558231&device_id=4389692076213352&luckycat_version_name=7.0.0-rc.13-sj1&luckycat_version_code=700131&status_bar_height=29#passport_csrf_token=73ea71317d6a88ae61544adcb22ec2f8;passport_csrf_token_default=73ea71317d6a88ae61544adcb22ec2f8;store-region=cn-jx;install_id=3767400127558231;ttreq=1$02dc3bfc858d7c9d09ef7f89e8dbbabc42f46299;odin_tt=988895483f3b530ba8234c6be4327a65d9f3aee862b8dd553fdaacb27c9cd78726e184b1f55ee11ee3e7986e7348bb647377d7048c966f851bdc1e9b115ef3fd70722c4e911152544e81cbea507c814d;n_mh=eeStMr--upDVKM0ec0Cs1ikuXQpLf7yIv0BgD0DrDQo;d_ticket=3c753fdef99e6631d930f4c42418a05b46087;sid_guard=5d6ebc62125dbb108bf8c38084bc50a1%7C1693792813%7C5184000%7CFri%2C+03-Nov-2023+02%3A00%3A13+GMT;uid_tt=e6926bb1cd9642b62cf031bb1a5ca71c;uid_tt_ss=e6926bb1cd9642b62cf031bb1a5ca71c;sid_tt=5d6ebc62125dbb108bf8c38084bc50a1;sessionid=5d6ebc62125dbb108bf8c38084bc50a1;sessionid_ss=5d6ebc62125dbb108bf8c38084bc50a1;store-region-src=uid#zH8S/68mAnMcOx8xYIv6b2xqi5MaoJvv0tL6SJdu5nhF9jpBji5JO1PQMgRffS49207wlsM2/ng0h+/AfbRI+NKtxOVJBTUGKcrYXnd3Fhtz8JRlx8mBz0n9Ad3CKVnvKA/fgfPaSAAJtusfZlFEE1pABXO8q1eLmFSNMasqPqaY1/jN+5uBrIEFgTcRxOcNCk4MGM34MfhSIhoTO3zBLn1JeEzsyTh01ltgjjPmsAunzWXjoW9dab8Vn9gy+K6C/J+LPgkvTToJp293PNyXJ3OL#ogrQFM2raGOZqKGV/yQ+bM/ITLx7ZCFZFLsdJ6kyzKsjUWMG"

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
