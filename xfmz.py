import os
import requests
def login():
    print(">>>>>开始登录账号<<<<<")
    url = 'http://xfmz.hfqx.xyz:85/home/index/login'
    headers = {
        'Host': 'xfmz.hfqx.xyz:85',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 Html5Plus/1.0',
        'Accept': '*/*',
        'Origin': 'http://xfmz.hfqx.xyz:85',
        'Referer': 'http://xfmz.hfqx.xyz:85/h5/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    xfmz = os.getenv('xfmz')
    account, pwd = xfmz.split('&')
    data = {
        'account': account,
        'pwd': pwd
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    if response_data['code'] == 1:
        token = response_data['token']
        wx_nickname = response_data['data']['wx_nickname']
        jade = response_data['data']['jade']
        rough = response_data['data']['rough']
        print("用户:", wx_nickname, "当前灵玉:", jade, "当前原石:", rough)
        return token
    else:
        print("登录失败")
        return None
def getPerTimeJade(token):
    print(">>>>>开始执行领取灵玉<<<<<")
    url = 'http://xfmz.hfqx.xyz:85/home/user/getPerTimeJade'
    headers = {
        'xfmz-token': token,
        'x-requested-with': 'XMLHttpRequest',
        'xfmz-id': '35389',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 Html5Plus/1.0',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'http://xfmz.hfqx.xyz:85',
        'Referer': 'http://xfmz.hfqx.xyz:85/h5/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        json_data = response.json()
        print(json_data['msg'])
    else:
        print('请求失败')
def tap(token):
    print(">>>>>执行领取原石<<<<<")
    url = 'http://xfmz.hfqx.xyz:85/home/card/tap'
    headers = {
        'xfmz-token': token,
        'x-requested-with': 'XMLHttpRequest',
        'xfmz-id': '35389',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 Html5Plus/1.0',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'http://xfmz.hfqx.xyz:85',
        'Referer': 'http://xfmz.hfqx.xyz:85/h5/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    response = requests.post(url, headers=headers, json={})
    data = response.json()
    print(data["msg"])
xfmz = os.getenv('xfmz')
if xfmz:
    print("偷你数据的脚本请谨慎运行")
    token = login()
    getPerTimeJade(token)
    tap(token)
else:
    print("请填写数据后重新运行")