from socket import *
import ntptime
import utime


def send_udp():
    # 同步时间
    ntptime.settime()

    # 获取当前时间
    t = utime.localtime()

    # 1. 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 2. 准备接收方的地址
    dest_addr = ('192.168.0.20', 8080)

    # 3. 从键盘获取数据
    send_data = "启动 " + str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])

    # 4. 发送数据到指定的电脑上
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    # 5. 关闭套接字
    udp_socket.close()
