'''
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm（抓不到数据的用黑盒不懂的联系我:3488790026)
new Env('创娱联盟'); 
'''
import requests
import os
import time

env_name = 'cylm'
env = os.getenv(env_name)

print("==========开始执行签到==========")

url1 = 'http://52.yyyy.run/api/sign/signTimeEnd'
headers1 = {
    'os': 'android',
    'token': env,
    'Content-Type': 'application/x-www-form-urlencoded',
}

task_ids = range(8960, 8964)

with requests.Session() as session1:
    session1.headers.update(headers1)
    for task_id in task_ids:
        data = {
            'task_id': str(task_id)
        }
        response = session1.post(url1, data=data)
        print(f"ID: {task_id}，运行返回：{response.text}")
        time.sleep(15)      
print("==========开始执行提现============")  
url2 = 'http://52.yyyy.run/api/user/postWith'
data2 = {'num': '1'}
headers2 = {
    'Referer': 'http://52.yyyy.run/pages/user/myWithdrawal.html',
    'Origin': 'http://52.yyyy.run',
}
headers2.update(headers1)

with requests.Session() as session2:
    session2.headers.update(headers2)
    response = session2.post(url2, data=data2)
    msg = response.json()['msg']
    result = f"提现结果：{msg}"
    print(result)