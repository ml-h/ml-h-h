#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# author: xm time:2020/10/15
import requests

url = "http://47.102.118.1:8089/api/challenge/create"

data = {
    "teamid":55 ,
    "data": {
        "letter": "g",
        "exclude": 7,
        "challenge": [
            [1, 3, 0],
            [6, 8, 4],
            [2, 5, 9]
        ],
        "step": 5,
        "swap": [6,9]
    },
    "token": "6ef4189d-40b3-476e-bcd6-ca9cd9b24ce0"
}

r = requests.post(url,json=data)
print(r.text)
