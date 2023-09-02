# -*- coding: utf-8 -*-
"""
cron: 1 6,22 * * *
new Env('昂立积分商城');

微信捉包https://points-mall.henshihui.com/ 请求头 cookie

青龙变量 export henshihui="PHPSESSID=xxxxxx" 多账号@隔开ANGLI
"""
import requests
import logging
import time
import os
import json
from notify import send

# 创建日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

cookies = []
try:
    if "henshihui" in os.environ:
        cookies = os.environ["henshihui"].split("@")
        if len(cookies) > 0:
            logger.info(f"共找到{len(cookies)}个账号 已获取并使用Env环境Cookie")
            logger.info("声明：本脚本为学习python 请勿用于非法用途")
    else:
        logger.info("【提示】变量格式: PHPSESSID=xxxxxx; snapshot=0\n 环境变量添加: henshihui")
        exit(3)
except Exception as e:
    logger.error(f"发生错误：{e}")
    exit(3)


# -------------------------分割线------------------------
class miniso:
    @staticmethod
    def setHeaders(i):
        headers = {
            'Host': 'points-mall.henshihui.com',
            'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; OPPO R9s Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5223 MMWEBSDK/20230701 MMWEBID/1571 MicroMessenger/8.0.40.2420(0x28002851) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'cookie': cookies[i]
        }
        return headers

    @staticmethod
    def tasklist(headers):
        try:
            url = f'https://points-mall.henshihui.com/task/api/show-app-task?pageSize=10&s_ver=1&applicationId=4066'
            response = requests.get(url=url, headers=headers)
            result = response.text
            json_data = json.loads(result)
            task_list = json_data['return_msg']['taskContent']['content']['task']['taskList']
            for task in task_list:
                task_name = task['taskName']
                if '邀' not in task_name:
                    task['limit'] = int(task['limit'])
                    task['rewardTimes'] = int(task['rewardTimes'])
                    num = task['limit'] - task['rewardTimes']
                    if task['rewardTimes'] < task['limit']:
                        taskKey = task['taskKey']
                        res = f"任务: {task['taskName']} -- 未完成"
                        logger.info(res)
                        log_list.append(res)
                        for _ in range(num):
                            miniso.task(headers, taskKey)
                            time.sleep(5)  # 休眠5秒
                    else:
                        res = f"任务: {task['taskName']} -- 已完成"
                        logger.info(res)
                        log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def task(headers, taskKey):
        try:
            url = f'https://points-mall.henshihui.com/task/api/report-task?taskKey={taskKey}&s_ver=1&applicationId=4066'
            data = {
                'taskKey': f'{taskKey}'
            }
            response = requests.post(url=url, headers=headers, data=data)
            result = response.json()
            res = f"上报: {result['return_msg']['msg']}"
            logger.info(res)
            log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def signin(headers):
        try:
            url = f'https://points-mall.henshihui.com/activity/sign-h5/sign?activityId=5520&s_ver=1&applicationId=4066'
            data = {
            'activityId': '5520',
            's_ver': '1',
            'applicationId': '4066'
        }
            response = requests.post(url=url, headers=headers, data=data)
            result = response.json()
            if result['return_code'] == 'SUCCESS':
                res = f"签到: 获得{result['return_msg']['prize']['pointsNum']}积分"
                logger.info(res)
                log_list.append(res)
            else:
                res = f"签到: {result['return_msg']}"
                logger.info(res)
                log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def my(headers):
        try:
            url = f'https://points-mall.henshihui.com/index/index/query-user-points?s_ver=1&applicationId=4066'
            response = requests.get(url=url, headers=headers)
            result = response.json()
            res = f"资产: 现有{result['return_msg']['points'][0]['points']}积分"
            logger.info(res)
            log_list.append(res)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    log_list = []  # 存储日志信息的全局变量
    for i in range(len(cookies)):
        logger.info(f"\n开始第{i + 1}个账号")

        logger.info("-------------任务开始-------------")
        headers = miniso.setHeaders(i)
        miniso.tasklist(headers)
        miniso.signin(headers)
        miniso.my(headers)

    logger.info("\n============== 推送 ==============")
    send("昂立积分商城", '\n'.join(log_list))
