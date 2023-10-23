'''
注册链接：https://52.yyyy.run//index/wechat/login/share_id/4063
抓token环境名字cylm（抓不到数据的用黑盒不懂的联系我:3488790026)
new Env('创娱联盟');（报错应该是完成任务了不要管，手动提现要去找客服激活直推0.3间接0.15要求完成签到）
解决已知问题
'''
import asyncio
import os
import requests

tokens = os.environ.get('cylm').split('@')
taskids = [''] * len(tokens)
msgs = [''] * len(tokens)

async def huoquguanggaoid(token, timeout=3, index=0):
    global taskids  
    url = 'https://52.yyyy.run/api/sign/getSignAd'
    headers = {
        'os': 'android',
        'token': token,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Host': '52.yyyy.run'
    }
    response = requests.post(url, headers=headers, timeout=timeout)
    result = response.json()
    if result['code'] == 1:
        taskids[index] = result['data']['task_id']
    return taskids

async def qiandao(token, timeout=3, index=0):
    print(f'开始执行第 {index+1} 个账号的签到任务\n')
    global taskids  
    if not taskids[index]:  
        await huoquguanggaoid(token, index=index)
    url = 'https://52.yyyy.run/api/sign/signTimeEnd'
    headers = {
        'os': 'android',
        'token': token,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '12',
        'Host': '52.yyyy.run'
    }
    body = f'task_id={taskids[index]}'
    response = requests.post(url, headers=headers, data=body, timeout=timeout)
    result = response.json()
    qdcode = result['code']
    if qdcode == 1:
        print(result['msg'], '\n')
        global msgs
        msgs[index] += result['msg'] + '\n'
    else:
        print('签到失败，正在尝试重新签到\n')
        msgs[index] += '签到失败，正在尝试重新签到\n'
        await huoquguanggaoid(token, index=index)
        await asyncio.sleep(6)
        await qiandao(token, index=index)
        await asyncio.sleep(20)

async def qiandaoshengyucishu(token, timeout=3, index=0):
    url = 'https://52.yyyy.run/api/sign/userSignData'
    headers = {
        'os': 'android',
        'token': token,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Host': '52.yyyy.run'
    }
    response = requests.post(url, headers=headers, timeout=timeout)
    result = response.json()
    if result['code'] == 1:
        ykcs = result['data']['today_sign']
        sycs = 3 - ykcs
    return sycs

async def chaxunyue(token, timeout=3, index=0):
    global msgs   
    print(f'开始查询第 {index+1} 个账号的余额\n')
    url = 'https://52.yyyy.run/api/user/index'
    headers = {
        'os': 'android',
        'token': token,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Host': '52.yyyy.run'
    }
    response = requests.post(url, headers=headers, timeout=timeout)
    result = response.json()
    if result['code'] == 1:
        allmoney = result['data']['all_money']
        print(f'当前金币余额：{allmoney}\n')
        msgs[index] += f'当前金币余额：{allmoney}\n'

async def tixian(token, timeout=3, index=0):
    global msgs   
    print(f'开始执行第 {index+1} 个账号的提现任务\n')
    url = 'https://52.yyyy.run/api/user/postWith'
    headers = {
        'os': 'android',
        'token': token,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '5',
        'Host': '52.yyyy.run'
    }
    body = 'num=2'   
    response = requests.post(url, headers=headers, data=body, timeout=timeout)
    result = response.json()
    if result['code'] == 1:
        print(result['msg'], '\n')
        msgs[index] += result['msg'] + '\n'
    else:
        print(f'提现失败，{result["msg"]}\n')
        msgs[index] += f'提现失败，{result["msg"]}\n'

async def main():
    tasks = []
    for i, token in enumerate(tokens):
        tasks.append(huoquguanggaoid(token, index=i))
    await asyncio.gather(*tasks)

    for i, token in enumerate(tokens):
        sycs = await qiandaoshengyucishu(token, index=i)
        for _ in range(sycs):
            await qiandao(token, index=i)

    tasks = []
    for i, token in enumerate(tokens):
        tasks.append(chaxunyue(token, index=i))
    await asyncio.gather(*tasks)

    tasks = []
    for i, token in enumerate(tokens):
        tasks.append(tixian(token, index=i))
    await asyncio.gather(*tasks)

asyncio.run(main())