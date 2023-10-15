''' 
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm
new Env('创娱联盟'); 
'''
import requests
import time
import random
import os

env_name = 'cylm' 
env = os.getenv(env_name)

url = 'http://52.yyyy.run/api/sign/signTimeEnd'
headers = {
    'os': 'android',
    'terminal': '2',
    'authorization': env,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip'
}

for task_id in range(8960, 8964):
    data = {'task_id': task_id}
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        result = response.json()
        msg = result.get('msg', '')
        print(f'签到结果: {msg}')
    else:
        print(f'Error processing Task ID {task_id}. Status code: {response.status_code}')
        
    delay = random.randint(15, 20)
    time.sleep(delay)