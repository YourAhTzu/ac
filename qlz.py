'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * 
new Env('巧乐兹'); 
环境变量名字qlz pushPlus通知环境变量tz
'''
import os
import requests
import time

accessToken = os.getenv("qlz")
pushPlusToken = os.getenv("tz")


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
        if "bonusPoints" in data:
            print(f"获得奖励积分数: {data['bonusPoints']}")
            push_message("签到成功")
        else:
            print("已签到")
    except Exception as e:
        print(f"签到出现异常: {e}")
        push_message("签到出现异常")


def share():
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
        for i in range(10):
            print(f"第 {i + 1} 次分享")
            response = requests.get(url, headers=headers)
            data = response.json()
            if response.status_code == 200 and data["code"] == 200:
                print("分享成功")
                push_message("分享成功")
            else:
                print("分享失败")
                push_message("分享失败")
            time.sleep(5)  # 延迟五秒
    except Exception as e:
        print(f"分享出现异常: {e}")
        push_message("分享出现异常")


def push_message(content):
    url = "https://www.pushplus.plus/send"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "token": pushPlusToken,
        "title": "巧乐兹",
        "content": content
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"推送消息响应: {response.text}")
    except Exception as e:
        print(f"推送消息出现异常: {e}")


def main():
    signin()
    share()


if __name__ == '__main__':
    main()
