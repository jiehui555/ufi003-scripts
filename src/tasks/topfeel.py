import random
import time
import requests
from src import config


__headers = {
    "sec-ch-ua-platform": '"Windows"',
    "Referer": "https://bbs.topfeel.com/h5/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    "Content-Type": "application/json",
    "token": config.TOPFEEL_TOKEN,
    "sec-ch-ua-mobile": "?0",
}


def auto_sign_in():
    url = "https://bbs.topfeel.com/api/gift/day_sign"
    payload = {
        "oldtime": int(time.time() * 1000),
        "newtime": int(time.time() * 1000) + random.randint(3000, 8000),
    }

    response = requests.post(url, headers=__headers, json=payload)

    print("状态码：", response.status_code)
    print("响应内容：", response.text)
