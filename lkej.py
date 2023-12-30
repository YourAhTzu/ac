'''
BY:YourAhTzu
完成日期:2023.12.30.12点
new Env('灵空二级域名分发系统');
抓X-CSRF-TOKEN和ck填入lkej多号@
'''
import os
import requests
tokens_cookies = os.environ.get('lkej').split('@')
for token_cookie in tokens_cookies:
    token, cookie = token_cookie.split('&')
    url = 'https://www.lkdns.top/home'
    headers = {
        'Host': 'www.lkdns.top',
        'Connection': 'keep-alive',
        'Content-Length': '12',
        'Accept': '*/*',
        'X-CSRF-TOKEN': token,
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.lkdns.top',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.lkdns.top/home',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': cookie
    }

    payload = {'action': 'sign'}
    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    if data['status'] == 0:
        print("签到成功")
    elif data['status'] == -1:
        print("已签到")