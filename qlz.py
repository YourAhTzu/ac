'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * 
new Env('巧乐兹'); 
'''
import os
import requests
import time

accessToken = os.getenv("qlz")

share_count = 0  # 已分享次数

def signin():
    print("开始执行签到")
    url = "https://kapi.yili.com/qlz/api/user/daily/sign?exParams=false"
    headers = {
        "Host": "kapi.yili.com",
        "Connection": "keep-alive",
        "accessToken": accessToken,
        "content-type": "application/x-www-form-urlencoded",
        "scene": "1089",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200 and data.get("bonusPoints"):
            print(f"获得奖励积分数: {data['bonusPoints']}")
        else:
            print("已签到")
    except Exception as e:
        print(f"签到出现异常: {e}")

def share():
    global share_count
    if share_count >= 10:  # 分享次数达到10次就不再执行
        return
    if share_count == 0:  # 只在第一次执行分享时打印消息
        print("开始执行分享")
    url = "https://kapi.yili.com/qlz/api/integral/product/share?productId=0"
    headers = {
        "Host": "kapi.yili.com",
        "Connection": "keep-alive",
        "accessToken": accessToken,
        "content-type": "application/x-www-form-urlencoded",
        "scene": "1089",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa206b57027b01b51/186/page-frame.html",
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200 and data["code"] == 200:
            print("分享成功")
            share_count += 1  # 已分享次数加一
        else:
            print("分享失败")
    except Exception as e:
        print(f"分享出现异常: {e}")

def lottery():
    print("开始执行抽奖")
    url = "https://kapi.yili.com/qlz/api/prize/turntable/draw?exParams=false&refreshTime=300"
    headers = {
        "Host": "kapi.yili.com",
        "Connection": "keep-alive",
        "accessToken": accessToken,  # 请确保accessToken已被定义并赋值
        "content-type": "application/x-www-form-urlencoded",
        "scene": "1089",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.41(0x1800292e) NetType/4G Language/zh_CN",
        "Referer": "https://servicewechat.com/wxa206b57027b01b51/186/page-frame.html",
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if response.status_code == 200 and data["code"] == 200:
            print(f"抽奖结果: {data.get('message')}")
        else:
            print("抽奖失败")
    except Exception as e:
        print(f"抽奖出现异常: {e}")

def main():
    is_signed = False
    for i in range(10):
        if not is_signed:
            signin()
            is_signed = True  # 只在第一次签到时打印信息
        share()
        if share_count >= 10:
            lottery()
        time.sleep(5)  # 分享和抽奖间隔时间为5秒

if __name__ == '__main__':
    main()
