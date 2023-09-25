'''
@YourAhTzu 
此接口调用小白API
功能：
1.自动存储驾宝考点题目（默认每次运行20题）
2.题目存储满20则自动清理
3.接口调用随机延迟5-10放置调用太大
4.诺不需要禁用任务即可
new Env('青龙闲得蛋疼系列-驾宝考点题目存储');
'''
import requests
import os
import random
import time

def main():
    url = "https://xiaobai.klizi.cn/API/other/jiakao.php?type=1" #默认科目一需要更改把1改为4

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    if not os.path.exists("tk.txt"):
        with open("tk.txt", "w", encoding="utf-8") as file:
            file.write("找不到tk.txt文件，已自动创建。\n")

        print("找不到tk.txt文件，已自动创建。")

    questions_count = 0  

    for i in range(20):
        existing_questions = []
        with open("tk.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for j in range(0, len(lines), 7):
                existing_questions.append(lines[j].strip())

        response = requests.get(url, headers=headers)
        current_question = response.json()["question"]

        if current_question not in existing_questions:
            question = response.json()["question"]
            answer = response.json()["answer"]
            explain = response.json()["explain"]
            type_info = response.json()["type"]
            chapter = response.json()["chapter"]

            with open("tk.txt", "a", encoding="utf-8") as file:
                questions_count += 1  
                file.write("第 %d 次存储：第 %d 题\n" % (i+1, questions_count))
                file.write("问题: " + question + "\n")
                file.write("答案: " + answer + "\n")
                file.write("解释: " + explain + "\n")
                file.write("题型: " + type_info + "\n")
                file.write("章节: " + chapter + "\n")
                file.write("\n====================\n\n")

            print("第 %d 次存储：第 %d 题已保存在 tk.txt 文件中。" % (i+1, questions_count))
        else:
            print("第 %d 次存储：题目已存在于 tk.txt 文件中，不再重复保存。" % (i+1))

        delay = random.randint(5, 10)
        print("等待 %d 秒..." % delay)
        time.sleep(delay)

if __name__ == '__main__':
    main()
