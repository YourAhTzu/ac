''' 
new Env('永辉生活');
此脚本仅供测试未完善
''' 
import requests
import time
import os
def flow(device_id, access_token):
    print(">>>>>果园签到<<<<<")
    timestamp = str(int(time.time() * 1000))    
    url = f"https://activity.yonghuivip.com/api/web/flow/farm/doTask?timestamp={timestamp}&channel=android&platform=android&v=9.12.0.12&sellerid=&deviceid={device_id}&shopid=9637&memberid=962892903519470906&app_version=9.12.0.12&channelSub=&brand=realme&model=RMX3562&os=android&osVersion=android31&networkType=WIFI&screen=2248*1080&productLine=YhStore&appType=h5&access_token={access_token}"
    headers = {
        "X-YH-Biz-Params": "xdotdy=--&gib=--,0(-$,&gvo=+$0_+)*,+",
        "X-YH-Context": "origin=h5&morse=1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36YhStore/9.12.0.12 cn.yonghui.hyd/2022952001 (client/phone; Android 31; realme/RMX3562)",
        "Content-Type": "application/json",
        "Origin": "https://m.yonghuivip.com",
        "X-Requested-With": "cn.yonghui.hyd",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.yonghuivip.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    payload = {
        "taskType": "sign",
        "activityCode": "HXNC-QG",
        "shopId": "",
        "channel": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    sign = data["data"]["signText"]
    print(f"果园签到结果:{sign}")
def member(device_id, access_token):
    print(">>>>>首页签到任务<<<<<")
    timestamp = str(int(time.time() * 1000))    
    url = f"https://api.yonghuivip.com/web/member/task/doTask?timestamp={timestamp}&channel=512&platform=wechatminiprogram&v=9.12.0.21&app_version=9.12.0.21&appid=wxc9cf7c95499ee604&wechatunionid=oCjU7wAne-c_Ymxw-7Do4KOQZKK4&deviceid={device_id}&sellerid=7&cityid=11&shopid=9637&channelSub=&brand=realme&model=RMX3562&os=android&osVersion=Android%2012&networkType=wifi&screen=1080*2364&productLine=YhStore&jysessionid=75913208-16ec-4e03-b653-30813c922021%23%2F&appType=h5&access_token={access_token}"
    headers = {
        "Host": "api.yonghuivip.com",
        "Connection": "keep-alive",
        "Content-Length": "54",
        "Accept": "application/json",
        "X-YH-Context": "origin=h5&morse=1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; RMX3562 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160027 MMWEBSDK/20231105 MMWEBID/2307 MicroMessenger/8.0.44.2502(0x28002C3F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxc9cf7c95499ee604",
        "Content-Type": "application/json",
        "Origin": "https://m.yonghuivip.com",
        "X-Requested-With": "com.tencent.mm",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.yonghuivip.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "taskId": 726,
        "shopId": "9637",
        "taskCode": "12yue-HYRW"
    }
    response = requests.post(url, json=data, headers=headers)
    data = response.json()
    if data["code"] == 1:
        print(f"签到成功: {data['data']['signed']}")
    else:
        print(f"签到失败: {data['message']}")
def main():
    tokens_str = os.environ.get('yhsh')
    if not tokens_str:
        print("请设置环境变量yhsh")
        return
    token_pairs = tokens_str.split('@')
    for pair in token_pairs:
        device_id, token = pair.split('&')
        flow(device_id, token)
        member(device_id, token)
        time.sleep(5)
        print("----------------------")
if __name__ == "__main__":
    main()