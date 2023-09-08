'''
@阿慈 仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
corn：10 10 * * *
'''
import os
import requests


# 设置请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
                  "MicroMessenger/8.0.40(0x18002831) NetType/4G Language/zh_CN",
    "Referer": "https://servicewechat.com/wxaa86961973acd21b/33/page-frame.html",
    "Content-Type": "application/json"
}


def send_video_request(video_num, renwu_id):
    nbb = os.environ.get("nbb").split('@')
    if not nbb:
        print("未设置环境变量 nbb")
        return
    
    url = f"https://sc.gdzfxc.com/?s=/ApiSign/videoRenwu&aid=1&platform=wx&session_id={nbb}&pid=0"
    data = {
        "renwu_id": renwu_id
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()

        status = response_data.get("status")
        msg = response_data.get("msg")
        scoreadd = response_data.get("scoreadd")

        print(f"第{video_num}个视频：")
        print(f"请求状态：{status}")
        print(f"消息：{msg}")
        print(f"积分：{scoreadd}")
        print("==============================")
    except:
        print(f"发送视频请求失败")


def main():
    renwu_ids = [1, 2, 3, 10]
    for i, renwu_id in enumerate(renwu_ids, start=1):
        send_video_request(i, renwu_id)


if __name__ == "__main__":
    main()
