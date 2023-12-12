'''
不拉人玩不了
'''
import os
import requests
import time
import re

def check():
    print("开始执行签到")
    url = "http://ss88.aaaabb0.cfd//index.php?m=user&c=index&a=picker"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://ss88.aaaabb0.cfd//",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": os.environ.get('ydd')
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    info = data["info"]
    print("签到结果：" + info)

def obtain():
    print("开始执行阅读")
    url = "http://ss88.aaaabb0.cfd/index.php?m=user&c=index&a=make_money_show"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Cookie': os.environ.get('ydd')
    }

    for _ in range(10):
        response = requests.get(url, headers=headers)
        data_payload = response.text
        id_match = re.search(r'id\s*:\s*(\d+)', data_payload)
        if id_match:
            read(id_match.group(1))
        time.sleep(5)

def read(id):
    url = "http://ss88.aaaabb0.cfd/index.php?m=user&c=browse&a=browse2"
    headers = {
        'Host': 'ss88.aaaabb0.cfd',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://ss88.aaaabb0.cfd',
        'Referer': 'http://ss88.aaaabb0.cfd/index.php?m=user&c=index&a=make_money_show',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': os.environ.get('ydd')
    }

    data = {
        'id': id 
    }

    response = requests.post(url, headers=headers, data=data)
    response_text = response.text
    pattern = r'<info>(.*?)</info>'
    match = re.search(pattern, response_text)

    if match:
        info = match.group(1)
        print(info)

check()
obtain()