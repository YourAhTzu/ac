import requests
import os
def gg():
    url = 'https://jihulab.com/Xiaoqinetwork/inform/-/raw/main/gg.txt'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
def Control():
    url = "https://jihulab.com/Xiaoqinetwork/inform/-/raw/main/Control.json"
    response = requests.get(url)
    data = response.json()
    v = data["zjgc"]["v"]
    open_status = data["zjgc"]["open"]
    if open_status == 0:
        print(data["zjgc"]["tz"])
        return False
    print(f"当前版本1.0，最新版本{v}")
    return True
def sign(membersession):
    url = "https://member-pro.zhengjiamax.com/memberSign/memberSign"
    headers = {
        'membersession': "VXIMG4UAIUVKHGVC8BFWWYSUPNHJHZR4"
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    msg = data["msg"]
    print(f"签到结果：{msg}")
def Info(membersession):
    url = "https://member-pro.zhengjiamax.com/member/getMemberInfo"
    headers = {
        'Content-Type': 'application/json',
        'membersession': "VXIMG4UAIUVKHGVC8BFWWYSUPNHJHZR4"
    }
    data = '{"memberInfoSource":2}'
    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    nickName = data["data"]["nickName"]
    initialBalance = data["data"]["initialBalance"]
    print(f"用户:{nickName}当前积分:{initialBalance}")
if __name__ == "__main__":
    membersession = os.environ.get('zjgc')
    if not membersession:
        print("请设置zjgc环境变量在运行")
    else:
        cks_list = membersession.split('@')
        num = len(cks_list)
        for num, ck in enumerate(cks_list, start=1):
            gg()
            print(f"=====开始执行第{num}个账号任务=====")
            if Control():
                print("=====开始执行签到任务=====")
                sign(membersession)
                print("=====开始执行分享任务=====")
                Info(membersession)