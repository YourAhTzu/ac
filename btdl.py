""" 
new Env('比特大陆');
零撸矿机神盘每天20U，够50U秒提各大交易所注册链接http://123.129.219.247:9898/mobile/reg/invite/613664
此脚本购买88矿机变量名btdl抓ck(有格局可以接码要换IP)
""" 
import os
import requests
import re

def buy_miner(number):
    url = 'http://123.129.219.247:9898/mobile/form.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36',
        'Referer': 'http://123.129.219.247:9898/mobile/form/id/162.html',
        'Cookie': number,
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

numbers = os.environ.get('btdl').split('@')

for i, number in enumerate(numbers, 1):
    print(f"第{i}个号码任务：{number}")
    buy_miner(number)