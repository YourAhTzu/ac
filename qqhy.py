""" 
new Env('洽洽会员俱乐部'); 
"""

import requests
import os

url = 'https://vip.qiaqiafood.com/vip/member/sign'

# 从环境变量中读取 Authorization 和 uid
authorization_uid = os.getenv('qqhy')

if authorization_uid:
    # 使用 & 分割小数据
    authorization, uid = authorization_uid.split('&')

    # 构造请求体数据
    requestData = {
        "channel": "",
        "uid": uid,
        "tenantId": "1"
    }

    # 请求头信息
    headers = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.40(0x18002831) NetType/WIFI Language/zh_CN",
        "Referer": "https://servicewechat.com/wxc72491b6cd007333/271/page-frame.html"
    }

    response = requests.post(url, json=requestData, headers=headers)

    print(response.json())
else:
    print("变量都没写忙着打飞机吗？")
