'''
账号密码登录
账号&密码(不支持多号垃圾盘)
'''
import os
import requests
def notice(): 
     try: 
         print(requests.get("https://ghproxy.smallfawn.top/https://raw.githubusercontent.com/YourAhTzu/ac/main/Notice.json", timeout=5).content.decode("utf-8")) 
     except requests.RequestException as e: 
         print(f"❗获取通知时出错: {e}")
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
    msg = response_data['msg']
    token = response_data['token']
    print(msg)
    return token
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
    notice()
    token = login()
    tap(token)
else:
    print("请填写数据后重新运行")