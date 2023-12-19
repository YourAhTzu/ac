"""
new Env('小猪惠选');
注册链接http://xiaozhu.tuesjf.cn/qrcode/NickBai5943341ac69104937493a7e2644d0208e688b.png
和火锅一样的自己看着玩变量名xzhx填token(自己看着定时任务未做全)
"""
import requests
import time
import random
import os
def video():
    print(">>>>>开始执行金币奖励<<<<<")
    url = 'http://xiaozhu.tuesjf.cn/apis/v1/lookVideo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/106/YM-RT/',
        'content-type': 'application/x-www-form-urlencoded',
        'Referer': 'http://m.xiaozhu.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    ids = [152, 153, 154, 155, 156, 157]
    for id in ids:
        data = {
            'id': str(id),
            'token': os.environ.get('xzhx') 
        }
        response = requests.post(url, headers=headers, data=data)
        json_data = response.json()
        msg = json_data['msg']
        print(f'{msg}')
        delay = random.randint(15, 25)
        time.sleep(delay)

def saveTankMoney():
    print(">>>>>开始执行广告奖励<<<<<")
    url = 'http://xiaozhu.tuesjf.cn/apis/v1/saveTankMoney'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/106/YM-RT/',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'http://m.xiaozhu.tuesjf.cn',
        'X-Requested-With': 'cn.tll.yyjx.xzdsp',
        'Referer': 'http://m.xiaozhu.tuesjf.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {
        'token': os.environ.get('xzhx')  
    }
    for _ in range(1):
        delay = random.randint(15, 25)
        time.sleep(delay)
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            data = response.json()
            if 'msg' in data:
                print(f"广告结果:{data['msg']}")

def LookRed():
    print(">>>>>开始执行红包奖励<<<<<")
    url = "http://xiaozhu.tuesjf.cn/apis/v1/LookRed"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36  XiaoMi/MiuiBrowser/10.8.1 LT-APP/45/106/YM-RT/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://m.xiaozhu.tuesjf.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "id": "20",
        "token": os.environ.get('xzhx')  
    }
    response = requests.post(url, headers=headers, data=data)
    json_data = response.json()
    msg = json_data["msg"]
    print(msg)

video()
saveTankMoney()
LookRed()
