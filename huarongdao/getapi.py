#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# author: xm time:2020/10/7
import json,requests,base64
import matplotlib.pyplot as plt
from PIL import Image

url = "http://47.102.118.1:8089/api/problem?stuid=031804114"
r = requests.get(url)
datadir = json.loads(r.text)

imgdata=base64.b64decode(datadir['img'])
path = r"D:\软工作业\get\\char.jpg"

file=open(path,'wb')
file.write(imgdata)
file.close()

img = Image.open(path)
plt.imshow(img)
plt.show()
