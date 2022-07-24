from socket import *

sockfd = socket()
sockfd.connect(('127.0.0.1', 8888))

# 读取目标文件，循环发送
f = open('time.txt','rb')
while True:
    data = f.read(1024)
    if not data:
        break
    sockfd.send(data)

f.close()
sockfd.close()