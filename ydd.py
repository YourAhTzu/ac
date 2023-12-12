#阅多多 一天一次手动提
import os
import requests
import time
import re
import json

def obtain():
    url = "http://ss88.aaaabb0.cfd/index.php?m=user&c=index&a=make_money_show"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Cookie': os.environ.get('ydd')
    }
    timestamp = int(time.time())
    url_with_timestamp = f"{url}&time={timestamp}"
    for _ in range(10):
        response = requests.get(url_with_timestamp, headers=headers)
        data_payload = response.text
        id_match = re.search(r'id\s*:\s*(\d+)', data_payload)
        if id_match:
            read(id_match.group(1))  # 将阅读ID作为参数传递给read函数
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
        'Referer': 'http://ss88.aaaabb0.cfd/index.php?m=user&c=index&a=make_money_show&time=1702358114',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': os.environ.get('ydd')
    }

    data = {
        'id': id  # 使用传入的阅读ID作为参数
    }

    response = requests.post(url, headers=headers, data=data)
    response_json = json.loads(response.text)

    info = response_json.get('info')
    if info:
        print(info)
    else:
        print("Failed to get reading earnings information")

obtain()
