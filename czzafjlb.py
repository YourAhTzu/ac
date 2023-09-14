'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * *
new Env('纯甄甄爱粉俱乐部');
'''
import requests
import json
import os

url = 'https://ucode-openapi.aax6.cn/lottery/checkIn'
headers = {
    'Content-Type': 'application/json',
    'appId': 'wx888d2a452f4a2a58',
    'Authorization': os.environ.get('czzafjlb'),
    'serialId': '528f8472-eda1-4fcc-8efc-99d28aaf016d'
}

data = {
    'promotionId': 1001117,
    'promotionCode': 'CRM-QD',
    'pointRecordRemark': '连续签到'
}

response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()

if response.status_code == 200:
    name = result.get('name')
    print(name)
elif response.status_code == 400:
    emsg = result.get('emsg')
    print(emsg)
