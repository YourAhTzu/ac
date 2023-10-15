'''
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm
new Env('创娱联盟'); 
'''
import requests
import os
import time
import random
import json

env_name = 'cylm'
env = os.getenv(env_name)

url = 'http://52.yyyy.run/api/sign/signTimeEnd'
headers = {
    'os': 'android',
    'terminal': '2',
    'token': env,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip'
}
for task_id in range(8960, 8964):
    data = {'task_id': task_id}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
​        result = response.json()
        result_json = json.dumps(result, ensure_ascii=False, indent=4)
    print(result_json)
    delay = random.randint(15, 20)