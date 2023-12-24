import os
import requests
def notice():
    try:
        print(requests.get("https://ghproxy.smallfawn.top/https://raw.githubusercontent.com/YourAhTzu/ac/main/Notice.json", timeout=5).content.decode("utf-8"))
    except requests.RequestException as e:
        print(f"❗获取通知时出错: {e}")
def login(account, pwd):
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
    notice()
    accounts = xfmz.split('@')
    for account in accounts:
        account_info = account.split('&')
        if len(account_info) == 2:
            token = login(account_info[0], account_info[1])
            if token:
                getPerTimeJade(token)
                tap(token)
            print("====================================")
        else:
            print("账号信息格式错误")
else:
    print("请填写数据后重新运行")