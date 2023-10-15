'''
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm（抓不到数据的用黑盒不懂的联系我:3488790026)
new Env('创娱联盟');（报错应该是完成任务了不要管，手动提现要去找客服激活直推0.5间接0.25要求完成签到）
解决已知问题
'''
import requests
import os
import time

env_name = 'cylm'
env = os.getenv(env_name)

print("==========开始执行签到==========")

url1 = 'http://52.yyyy.run/api/sign/getSignAd'
headers1 = {
    'os': 'android',
    'appid': '',
    'terminal': '2',
    'token': env,  
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; V2068A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/29.0)',
    'Content-Type': 'application/x-www-form-urlencoded',
}

url2 = 'http://52.yyyy.run/api/sign/signTimeEnd'
headers2 = {
    'os': 'android',
    'token': env,
    'Content-Type': 'application/x-www-form-urlencoded',
}

url3 = 'http://52.yyyy.run/api/user/postWith'
data3 = {'num': '1'}
headers3 = {
    'Referer': 'http://52.yyyy.run/pages/user/myWithdrawal.html',
    'Origin': 'http://52.yyyy.run',
}
headers3.update(headers2)

with requests.Session() as session:
    session.headers.update(headers1)
    for _ in range(3):
        response = session.post(url1)
        task_id = response.json()['data']['task_id']
        print(f"获取到的task_id为：{task_id}")

        session.headers.update(headers2)
        data2 = {'task_id': str(task_id)}
        response = session.post(url2, data=data2)
        print(f"ID: {task_id}，运行返回：{response.text}")
        time.sleep(15)

    session.headers.update(headers3)
    response = session.post(url3, data=data3)
    msg = response.json()['msg']
    result = f"提现结果：{msg}"
    print(result)