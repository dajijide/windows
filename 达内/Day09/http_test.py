from socket import *
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(3)

c, addr = s.accept()
print("Connect from...",addr)
data = c.recv(4096) # 接收http請求
print(data)

# 将数据组织为响应格式
response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Hello world</h1>
"""
c.send(response.encode())  # 发送响应内容
c.close()
s.close()