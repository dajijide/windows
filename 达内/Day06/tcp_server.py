import socket
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

sockfd.bind(('127.0.0.1', 11111))
sockfd.listen(7)
print("waiting for connect")
connfd, addr = sockfd.accept()
print("connect from",addr)
date = connfd.recv(1024)