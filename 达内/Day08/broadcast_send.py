"""
接收广播
1.创建udp套接字
2.设置可以发送广播
3.循环向广播地址发送
"""
import time
from socket import *

# 创建广播
dest = ('172.40.91.255', 9999)

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

data = """"
            ******
            啦啦啦
"""

while True:
    time.sleep(2)
    s.sendto(data.encode(), dest)  # 目标地址=广播地址

