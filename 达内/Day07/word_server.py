"""
使用UDP客户端查询单词，得到单词解释，
如果没有单词就得到”没有单词“。
客户可以循环输入单词，直到输入值为空

"""
# 创建套接字
from socket import *


def find_word(word):
    f = open('dict.txt')
    for line in f:
        w = line.split(' ')[0]
        # 如果遍历到的单词已经大于word就结束查找
        if w > word:
            f.close()
            return "没有找到单词"
        elif w == word:
            f.close()
            return line
    else:
        f.close()
        return "没有找到单词"


# 绑定地址
sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd_addr = ('127.0.0.1', 8889)
sockfd.bind(sockfd_addr)

# 循环收发消息
while True:
    # data接收的单词
    data, addr = sockfd.recvfrom(1024)
    # 查单词
    result = find_word(data.decode())
    sockfd.sendto(result.encode(), addr)

# 关闭套接字
sockfd.close()
