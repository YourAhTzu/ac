'''
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm
new Env('创娱联盟'); 
'''
import requests
import time
import os

env_name = 'cylm'
env = os.getenv(env_name)

url = 'http://52.yyyy.run/api/sign/signTimeEnd'
headers = {
    'os': 'android',
    'appid': '',
    'terminal': '2',
    'token': env,
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/29.0)',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip'
}

task_ids = range(8960, 8964)

for task_id in task_ids:
    data = {
        'task_id': str(task_id)
    }
    response = requests.post(url, headers=headers, data=data)
    # 处理响应结果
    print(f"Task ID: {task_id}，运行返回：{response.text}")
    time.sleep(15) 