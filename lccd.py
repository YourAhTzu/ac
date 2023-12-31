'''
BY:YourAhTzu
完成日期:12.31 下午13:21
new Env('莱充充电');
一天一次抓authorization的JWT后面数据填入lccd变量
'''
import os
import requests
def main():
    authorization = os.environ.get('lccd')
    numbers = authorization.split('@')
    for number in numbers:
        print(f">>>>开始执行莱充充电任务<<<<<")
        userinfo(number)
        signComplete(number)
        pointsDouble(number)
        taskComplete(number)
def userinfo(number):
    print(f">>>>用户查询<<<<<")
    url = 'https://shop.laichon.com/api/v1/member/userinfo'
    headers = {
        'Host': 'shop.laichon.com',
        'Connection': 'keep-alive',
        'authorization': f'JWT {number}',
        'charset': 'utf-8',
        'service-code': 'WYC-MI-WEIXIN',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002CCA) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wxa68db1dabe823e7e/316/page-frame.html'
    }
    data = {}
    response = requests.get(url, headers=headers, data=data)
    json_response = response.json()
    mobile = json_response['data']['mobile']
    points = json_response['data']['points']
    print(f"用户:{mobile}", f"当前积分:{points}")
def signComplete(number):
    print(f">>>>开始执行签到<<<<<")
    url = 'https://shop.laichon.com/api/v1/task/signComplete'
    headers = {
        'Host': 'shop.laichon.com',
        'Connection': 'keep-alive',
        'authorization': f'JWT {number}',
        'charset': 'utf-8',
        'service-code': 'WYC-MI-WEIXIN',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002CCA) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wxa68db1dabe823e7e/316/page-frame.html'
    }
    data = {}
    response = requests.get(url, headers=headers, data=data)
    json_response = response.json()
    msg = json_response.get('msg')
    print(f"签到结果:{msg}")
def pointsDouble(number):
    print(f">>>>开始执行签到翻倍<<<<<")
    url = 'https://shop.laichon.com/api/v1/task/pointsDouble'
    headers = {
        'Host': 'shop.laichon.com',
        'Connection': 'keep-alive',
        'authorization': f'JWT {number}',
        'charset': 'utf-8',
        'service-code': 'WYC-MI-WEIXIN',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002CCA) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wxa68db1dabe823e7e/316/page-frame.html'
    }
    data = {}
    response = requests.get(url, headers=headers, data=data)
    json_response = response.json()
    msg = json_response.get('msg')
    print(f"签到翻倍结果:{msg}")
def taskComplete(number):
    print(f">>>>开始执行看广告<<<<<")
    url =  'https://shop.laichon.com/api/v1/task/taskComplete'
    headers = {
        'Host': 'shop.laichon.com',
        'Connection': 'keep-alive',
        'authorization': f'JWT {number}',
        'charset': 'utf-8',
        'service-code': 'WYC-MI-WEIXIN',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002CCA) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wxa68db1dabe823e7e/316/page-frame.html'
    }
    data = {
        'task_id': 4
    }
    response = requests.post(url, headers=headers, data=data)
    json_response = response.json()
    msg = json_response.get('msg')
    print(f"看广告结果:{msg}")
if __name__ == '__main__':
    main()