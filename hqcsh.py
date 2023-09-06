""
​
time：2023.4.26
cron: 0 9,18 * * *
new Env('好奇车生活签到');
微信小程序-好奇车生活-好物兑换
抓包域名: https://channel.cheryfs.cn/
抓包请求头里面: accountId 的值
环境变量名称：hqcshck = accountId 的值
多账号新建变量或者用 & 分开
​底部已更新concurrency并发次数自行更改
"""
import os
import requests
import time
import json
import threading


class Hqcsh:
    def __init__(self, ck):
        self.session = requests.Session()
        self.ck = ck
        self.base_url = "https://tk3q5wwu74.execute-api.us-east-1.amazonaws.com"
        self.user_info = None
        
        # 加载内置请求头和 cookie
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/58.0.3029.110 Safari/537.36 ",
            "cookie": f"token={self.ck}"
        }
    
    def sign(self):
        url = f"{self.base_url}/prod/sign"
        resp = self.session.post(url, headers=self.headers)
        
        msg = ''
        if resp.status_code == 200:
            res_json = json.loads(resp.content.decode('utf-8'))
            if res_json['status'] == "success":
                self.user_info = res_json["data"]["user_info"]
                today_sign_days = self.user_info.get("today_sign_days")
                total_sign_days = self.user_info.get("total_sign_days")
                
                msg += f"今天签到成功，已连续签到 {today_sign_days} 天，累计签到 {total_sign_days} 天\n"
            else:
                msg += f"签到失败，信息：{res_json}\n"
        else:
            resp.raise_for_status()
            
        return msg
    
    def qiang(self, qiang):
        self.headers["Referer"] = "https://www.haoqiche.com/"
        url = f"{self.base_url}/prod/gift"
        data = {"gift_id": qiang}
        resp = self.session.post(url, json=data, headers=self.headers)
        
        result = None
        if resp.status_code == 200:
            res_json = json.loads(resp.content.decode('utf-8'))
            if res_json['status'] == "success":
                gift_name = res_json["data"]["gift_info"]["name"]
                result = f"恭喜，您抢到了【{gift_name}】的礼包！"
            else:
                err_msg = res_json.get("msg")
                if err_msg == '积分不足':
                    result = "抢包失败，积分不足"
                else:
                    result = f"抢包失败，信息：{res_json}"
        else:
            resp.raise_for_status()
            
        return result


def get_environ(key):
    try:
        with open(".env.json", encoding="utf-8") as f:
            env = json.load(f)
        return env[key]
    except Exception as e:
        print(f"获取环境变量 {key} 失败:", e)
        return ""


def send(title, content):
    sckey = get_environ("sckey")
    if not sckey:
        print("没有配置 Server 酱，无法推送消息")
        return

    url = f"https://sc.ftqq.com/{sckey}.send"
    data = {
        "text": title,
        "desp": content
    }

    try:
        resp = requests.post(url, data=data)
        resp_json = resp.json()
        if resp_json["errno"] == 0:
            print("推送成功")
        else:
            print(f"推送失败: {resp_json}")
    except Exception as e:
        print("推送消息时出错:", e)


def run_sign(ck):
    run = Hqcsh(ck)
    return run.sign()


def run_qiang(ck, qiang):
    run = Hqcsh(ck)
    result = run.qiang(qiang)
    if result is not None:
        print(f"抢包结果：{result}")
        if send:
            send("好奇车生活签到通知", f"抢包结果：{result}")


def auto_run(concurrency, loop):
    q1 = '647894196522340352'  # 188积分 1.08元
    q2 = '622187839353806848'  # 288积分 1.88元
    q3 = '622187928306601984'  # 588积分 3.88元
    q4 = '622188100122075136'  # 888积分 5.88元
    
    qiang = q4  # 默认设置自动抢888积分5.88元的包
    
    print('\n默认设置自动抢888积分5.88元的包\n需要设置到脚本底部修改 qiang = xxx\nxxx为q1-q4对应的包\n')
    
    token = get_environ("hqcshck")
    msg = ''
    cks = token.split("&")
    
    for ck in cks:
        msg += run_sign(ck)
    
    success_count = 0
    while success_count < concurrency:
        threads = []
        for ck in cks:
            thread = threading.Thread(target=run_qiang, args=(ck, qiang))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
            success_count += 1
        
        if success_count >= concurrency:
            break
        
        print("未成功抢到包，等待5秒后再次尝试...")
        time.sleep(5)  # 未抢到包时等待5秒后继续循环
    
    if send:
        send("好奇车生活签到通知", msg + f"\n并发抢包完成，成功抢到包的账户数量：{success_count}")


if __name__ == '__main__':
    auto_run(concurrency=2, loop=10)
