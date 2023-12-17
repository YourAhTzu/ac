""" 
new Env('比特大陆');
零撸矿机神盘每天20U，够50U秒提各大交易所注册链接http://123.129.219.247:9898/mobile/reg/invite/613664
此脚本购买88矿机变量名btdl抓ck(有格局可以接码要换IP)
""" 
import os
import requests
import re
cks = os.environ.get('btdl').split('@')
for i, ck in enumerate(cks, start=1):
    print(f"开始运行第{i}个账号任务")
    url = 'http://123.129.219.247:9898/user/person.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 12; zh-cn; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 HeyTapBrowser/40.7.37.9',
        'Referer': 'http://123.129.219.247:9898/mobile/login.html',
        'Cookie': ck,
    }
    response = requests.get(url, headers=headers)
    html = response.text
    pattern_username = r'<div class="t2">(.*?)<!--'
    match_username = re.search(pattern_username, html)
    if match_username:
        username = match_username.group(1)
    pattern_balance = r'<div class="t3">(.*?)</div>'
    match_balance = re.search(pattern_balance, html)
    if match_username:
    username = match_username.group(1)
    print("{}, 当前余额{}".format(username, balance))
else:
    print("未能获取用户名")
    url = 'http://123.129.219.247:9898/mobile/form.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36',
        'Referer': 'http://123.129.219.247:9898/mobile/form/id/162.html',
        'Cookie': ck,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'id': '162',
        'money': '1'
    }
    response = requests.post(url, headers=headers, data=data)
    string = response.text
    pattern = r'<p.*?>(.*?)</p>'
    result = re.findall(pattern, string)
    if result:
        print(f"购买结果：{result[0]}")