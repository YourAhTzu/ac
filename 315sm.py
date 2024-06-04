'''
new Env('315监控');
没啥卵用就是发一些零撸的东西
'''
import requests
import re
import sys
from os import path
def load_send():
    global send
    cur_path = path.abspath(path.dirname(__file__))
    send_module_path = cur_path + "/SendNotify.py"
    if path.exists(send_module_path):
        from SendNotify import send
        print("加载通知服务成功！")
    else:
        print("未找SendNotify.py文件即将推出运行")
        sys.exit()
def ac():
    url = "https://www.315som.com/category/ll"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 14; zh-cn; RMX3562 Build/UKQ1.230924.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 HeyTapBrowser/40.8.30.3",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    response = requests.get(url, headers=headers)
    html_content = response.text

    pattern = re.compile(r'<h2 class="item-heading"><a href="(https://www\.315som\.com/\d+\.html)">(.*?)</a></h2>')
    matches = pattern.findall(html_content)
    content = ""
    for match in matches:
        link, title = match
        content += f"项目名称: {title}\n项目地址: {link}\n\n"
    return content
if __name__ == "__main__":
    load_send()
    content = ac()
    send("大人请查收今日零撸项目", content)