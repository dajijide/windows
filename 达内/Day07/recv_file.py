from socket import *

s = socket()
s.bind(('127.0.0.1', 8888))
s.listen(5)

c,addr = s.accept()
print("Connet from", addr)
file = open('test.txt', 'wb')

# 循环接收写入文件
while True:
    data = c.recv(1024)
    file.write(data)
    if not data:
        break

file.close()
c.closr()
s.close()