"""
udp 服务端流程
"""
# 创建套接字
from socket import *

# 绑定地址
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd_addr = ('127.0.0.1', 8887)
sockfd.bind(sockfd_addr)

# 循环收发消息
while True:
    date, addr = sockfd.recvfrom(1024)
    print("收到消息：", date.decode())
    sockfd.sendto(b'Thanks', addr)

# 关闭套接字
sockfd.close()
