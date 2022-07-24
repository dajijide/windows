"""
使用udp完成，客户端不断录入学生信息
将其发送到服务端，服务端将学生信息写入到一个文件中，每个学生信息占一行
"""
from socket import *
import struct

# 和客户端一致
st = struct.Struct('i32sif')

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(('127.0.0.1', 8888))

# 打开文件
f = open('student.txt', 'a')

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(4096)
    # (1, b'lily', 16, 89.5)
    data = st.unpack(data)

    # 写入文件
    info = "%d %-10s %d %.1f\n" % data
    f.write(info)
    f.flush()
# 关闭套接字
sockfd.close()