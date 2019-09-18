#!user/bin/python3
# 文件名:server.py

import socket
import sys

# socket.socket([family[, type[, proto]]])
# Socket是介于应用层和传输层之间
# 参数
# family: 套接字家族可以使AF_UNIX或者AF_INET
# 源IP地址和目的IP地址以及源端口号和目的端口号的组合称为套接字
# 地址家族（address family，AF）：
#
#   AF_UNIX == AF_LOCAL UNIX 套接字，BSD套接字
#   AF_INET IPv4套接字
#   AF_INET6 IPv6套接字
#   AF_NETLINK 使用标准的BSD套接字接口进行用户级别和内核级别代码之间的IPC
#   AF_TIPC 透明的进程间通信
# type: 套接字类型可以根据是面向连接的还是非连接分为 SOCK_STREAM 或 SOCK_DGRAM
# protocol: 一般不填默认为0.


# 创建socket对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 获取本地主机名
host=socket.gethostname()
port=9999

# 绑定端口号
serversocket.bind((host,port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr=serversocket.accept()
    print("连接地址为: %s" % str(addr))
    msg='欢迎访问...Morain?'+'\r\n'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()









