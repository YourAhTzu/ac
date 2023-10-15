'''
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm
new Env('创娱联盟'); 
'''
import requests
import os
import time

env_name = 'cylm'
env = os.getenv(env_name)

url = 'http://52.yyyy.run/api/sign/signTimeEnd'
headers = {
    'os': 'android',
    'token': env,
    'Content-Type': 'application/x-www-form-urlencoded',
}

task_ids = range(8960, 8964)

with requests.Session() as session:
    session.headers.update(headers)
    for task_id in task_ids:
        data = {
            'task_id': str(task_id)
        }
        response = session.post(url, data=data)
        print(f"ID: {task_id}，运行返回：{response.text}")
        time.sleep(15) 
    
    
url = 'http://52.yyyy.run/api/user/postWith'
data = {'num': '1'}
headers['Referer'] = 'http://52.yyyy.run/pages/user/myWithdrawal.html'
headers['Origin'] = 'http://52.yyyy.run'

with requests.Session() as session:
    session.headers.update(headers)
    response = session.post(url, data=data)
    msg = response.json()['msg']
    result = f"提现结果：{msg}"
    print(result)