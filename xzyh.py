"""
new Env('小猪惠选');
注册链接http://xiaozhu.tuesjf.cn/qrcode/NickBai5943341ac69104937493a7e2644d0208e688b.png
和火锅一样的自己看着玩变量名xzhx_token填token
"""

import requests
import time
import os
import json
import random
import datetime
from concurrent.futures import ThreadPoolExecutor

BF = False
yc = tuple(map(int, os.environ.get('xzyc', '20,28').split(',')))

class XZHX:
    def __init__(self, ck1):
        self.token = ck1
        self.ua = "Mozilla/5.0 (Linux; Android 14; 23078RKD5C Build/UP1A.230905.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/106/YM-RT/"
        self.hd = {
            'Host': 'xiaozhu.tuesjf.cn',
            'Connection': 'keep-alive',
            'User-Agent': self.ua,
            'content-type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Origin': 'http://m.xiaozhu.tuesjf.cn',
            'X-Requested-With': 'cn.tll.yyjx.xzdsp',
            'Referer': 'http://m.xiaozhu.tuesjf.cn/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
        }

    ##登录
    def login(self):
        url = f'http://xiaozhu.tuesjf.cn/apis/v1/user_info?token={self.token}'
        r = requests.get(url, headers=self.hd).json()
        msg = r["msg"]
        if msg == "获取成功":
            name = r["data"]["info"]["nickname"]
            balance = r["data"]["info"]["balance"]
            gold = r["data"]["info"]["gold"]
            integral = r["data"]["info"]["integral"]
            rname = r["data"]["info"]["rank_name"]
            print(f"账号[{name}]登录成功--账户等级[{rname}]--储蓄金余额[{gold}]--我的零钱[{balance}]--金币余额[{integral}]")
            k = str(integral).split(".")[0]
            if 7 <= datetime.datetime.now().hour <= 9:
                print("----开始签到----")
                self.signid(name)
                time.sleep(4)
            if 21 <= datetime.datetime.now().hour <= 23:
                print("----进行金币兑换----")
                self.jbdh(name, k)
                time.sleep(4)
            print("----开始领取金币奖励----")
            self.ids(name)
            time.sleep(4)
            print("----开始领取广告奖励----")
            self.ggjl(name)
        else:
            print(f'登录失败: {r["msg"]}')

    ##获取任务id
    def ids(self, m):
        try:
            url = f'http://xiaozhu.tuesjf.cn/apis/v1/updateActive?token={self.token}'
            r = requests.get(url, headers=self.hd).json()
            id_list = [item['id'] for item in r['data']['list']]
            hbid = r["data"]["red_order"]["id"]
            for y in id_list:
                time.sleep(self.yc_time())
                r = self.jbjl(m, y)
                if r in ["该任务奖励已达上限", "当前已领取请勿重复领取"]:
                    break
            time.sleep(4)
            print("----开始领取红包奖励----")
            self.hbjl(m, hbid)
        except json.decoder.JSONDecodeError as e:
            print(f"{e}")

    ##获取签到id
    def signid(self, m):
        try:
            url = f'http://xiaozhu.tuesjf.cn/apis/v1/indexSignShow?token={self.token}'
            r = requests.get(url, headers=self.hd).json()
            qdids = [item['id'] for item in r['data']]
            for s in qdids:
                time.sleep(3)
                r = self.sign(m, s)
                if r == "今日已签到":
                    break
        except json.decoder.JSONDecodeError as e:
            print(f"{e}")

    ##签到
    def sign(self, m, s):
        try:
            url = 'http://xiaozhu.tuesjf.cn/apis/v1/signSave'
            data = {'id': s, 'token': self.token}
            re = requests.post(url, headers=self.hd, data=data).json()
            msg = re["msg"]
            print(f"[{m}]签到: {msg}")
            return msg
        except json.decoder.JSONDecodeError as e:
            print(f"{e}")

    ##金币奖励
    def jbjl(self, m, t):
        try:
            url = 'http://xiaozhu.tuesjf.cn/apis/v1/lookVideo'
            data = {'id': t, 'token': self.token}
            re = requests.post(url, headers=self.hd, data=data).json()
            msg = re["msg"]
            print(f"[{m}]领取金币奖励[{t}]: {msg}")
            return msg
        except json.decoder.JSONDecodeError as e:
            print(f"{e}")

    ##广告奖励
    def ggjl(self, m):
        for u in range(3):
            try:
                url = "http://xiaozhu.tuesjf.cn/apis/v1/saveTankMoney"
                data = {
                    'token': self.token
                }
                r = requests.post(url, headers=self.hd, data=data).json()
                msg = r["msg"]
                print(f"[{m}]第{u}领取广告奖励：{msg}")
                if msg == "该任务奖励已达上限":
                    break
                time.sleep(self.yc_time())
            except json.decoder.JSONDecodeError as e:
                print(f"{e}")

    ##红包奖励
    def hbjl(self, m, h):
        try:
            url = 'http://xiaozhu.tuesjf.cn/apis/v1/LookRed'
            data = {
                'id': h,
                'token': self.token
            }
            r = requests.post(url, headers=self.hd, data=data).json()
            msg = r["msg"]
            print(f"[{m}]领取红包奖励: {msg}")
        except json.decoder.JSONDecodeError as e:
            print(f"{e}")

    ##金币兑换
    def jbdh(self, m, k):
        try:
            url = 'http://xiaozhu.tuesjf.cn/apis/v1/receiveVideo'
            data = {'num': k, 'token': self.token}
            re = requests.post(url, headers=self.hd, data=data).json()
            msg = re["msg"]
            print(f"[{m}]金币兑换: {msg}")
            return msg
        except json.decoder.JSONDecodeError as e:
            print(f"{e}")

    def yc_time(self):
        q_time, j_time = yc
        yc_time1 = random.randint(q_time, j_time)
        return yc_time1

if __name__ == "__main__":
    def BF1(ck):
        xzhx = XZHX(ck)
        xzhx.login()
    if 'xzhx_token' in os.environ:
        cookie = os.environ.get("xzhx_token")
    else:
        print("变量[xzhx_token]不存在,请设置[xzhx_token]变量后运行")
        exit(-1)
    cookies = cookie.split("&")
    i = 1
    print(f"小猪惠选共获取到{len(cookies)}个账号")

    if BF:
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(BF1, cookies)
            n = random.uniform(4, 6)
            print(f'{n}s后进行下一个账号')
            time.sleep(n)
    else:
        for ck in cookies:
            print(f"------账号{i}-----")
            XZHX(ck).login()
            if i < len(cookies):
                i += 1
                n = random.uniform(4, 6)
                print(f'{n}s后进行下一个账号')
                time.sleep(n)