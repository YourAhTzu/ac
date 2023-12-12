import requests
import hashlib
import time
import os

withdraws_item_id = '30'  #默认30

def notice():
    print("=====开始获取远程公告====")
    url = "https://ghproxy.smallfawn.top/https://raw.githubusercontent.com/YourAhTzu/ac/main/Notice.json"
    try:
        response = requests.get(url)
        data = response.text
        print(data)
    except requests.RequestException as e:
        print(f"Error occurred while fetching notice: {e}")

def finish(taskId, cookie, account_index):
    timestamp = int(time.time())
    sign = hashlib.md5(f'7b7fpld4roey0e6e&taskId={taskId}&time={timestamp}'.encode()).hexdigest()
    url = f"http://api.ibreader.com/task_api/task/finish"
    headers = {
        'Host': 'api.ibreader.com',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCAM00 Build/NGI77B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
        'X-Client': 'sv=7.1.2;pm=PCAM00;ss=1080*2196;version=5.1.86.18.130500001;vId=60752445880d4366988c18aa9d9f6b80;signVersion=2;webVersion=new;oaid=null;pkv=1;ddid=DUzp43Y2YF9X-5bmS5YXSEZcB3nELTOxTV04RFV6cDQzWTJZRjlYLTVibVM1WVhTRVpjQjNuRUxUT3hUVjA0c2h1;androidosv=25;os=0;muk=ui98HJmkunswcEuBWDlg3A%3D%3D;firm=OPPO;duk=Bv6b4gAgfXcjaj%2BBwEtH32pUNNCFZYDKNOv%2Boplr96Q%3D;',
        'Referer': 'https://api.ibreader.com/task_api/task/getChapterTaskList',
        'Accept-Encoding': 'gzip, deflate',
    }
    data = {
        'time': timestamp,
        'sign': sign,
        'taskId': taskId,
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        if result['code'] == 100:
            if result['data']['rewardNum'] > 0:
                print(f"\n恭喜获得:{result['data']['rewardNum']}金币")
        elif result['code'] == 180:
            print("任务已完成")
    except requests.exceptions.RequestException as e:
        print("请求异常:", e)
def withdraw(cookie, account_index):
    timestamp = str(int(time.time()))
    sign = hashlib.md5(('7b7fpld4roey0e6e&itemId=' + withdraws_item_id + '&platform=0&time=' + timestamp).encode()).hexdigest()
    url = f"https://increase.ibreader.com/task_api/task/v1/withdraw/valid"
    headers = {
        'Host': 'api.ibreader.com',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded; Charset=UTF-8',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; PCAM00 Build/NGI77B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36',
        'X-Client': 'sv=7.1.2;pm=PCAM00;ss=1080*2196;version=5.1.86.18.130500001;vId=60752445880d4366988c18aa9d9f6b80;signVersion=2;webVersion=new;oaid=null;pkv=1;ddid=DUzp43Y2YF9X-5bmS5YXSEZcB3nELTOxTV04RFV6cDQzWTJZRjlYLTVibVM1WVhTRVpjQjNuRUxUT3hUVjA0c2h1;androidosv=25;os=0;muk=ui98HJmkunswcEuBWDlg3A%3D%3D;firm=OPPO;duk=Bv6b4gAgfXcjaj%2BBwEtH32pUNNCFZYDKNOv%2Boplr96Q%3D;',
        'Referer': 'https://api.ibreader.com/task_api/task/getChapterTaskList',
        'Accept-Encoding': 'gzip, deflate',
    }
    data = {
        'itemId': withdraws_item_id,
        'platform': '0',
        'sign': sign,
        'time': timestamp,
    }
    response = requests.post(url, headers=headers, data=data)
    try:
        result = response.json()
        if result['code'] == 100:
            print(f"提现成功: ✅, {result['msg']}")
        else:
            print(f"提现失败: ❌, 原因是：{result['msg']}")
    except Exception as e:
        print(f"信息异常: ❌, {response.text}, 原因：{e}")

notice()
task_ids = [1,3,8,96, 97, 98, 99, 100, 101, 102, 103, 104, 105,201,202,203,204,205,206,233, 234, 235, 236, 237, 238,490]
bkxs_accounts = os.environ.get('bkxs').split('&') 
for account_index, account in enumerate(bkxs_accounts, start=1):
    print(f"===开始执行第{account_index}账号任务===")
    for task_id in task_ids:
        finish(task_id, account, account_index)
    withdraw(account, account_index)