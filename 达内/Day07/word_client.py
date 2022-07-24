"""
udp 客户端流程
"""
from socket import *

ADDR = ('127.0.0.1', 8889)

sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Word>>")
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom((1024))
    print("From server:", msg.decode())

sockfd.close()