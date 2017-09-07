import socket
import time
import threading
import feiQ_data
import send_online_msg
import send_offline_msg
import send_message
import recv_msg


def create_socket():
    """创建套接字并绑定端口，设置允许广播"""
    feiQ_data.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ("", 1357)
    feiQ_data.udp_socket.bind(local_addr)
    feiQ_data.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def close_socket():
    """关闭套接字"""
    feiQ_data.udp_socket.close()


def my_choice():
    """获取用户的选择"""
    print("输入1上线，输入2下线，输入3发送消息，输入4退出")
    option = input("输入选项")
    return option


def main():
    """控制程序"""
    #创建套接字
    create_socket()
    #创建子线程对象
    nostop_recv = threading.Thread(target=recv_msg.receive_message)
    #运行子线程
    nostop_recv.start()
    while True:
        choice = my_choice()
        #发送上线消息
        if choice == "1":
            send_online_msg.send_onlinemsg()
        #发送离线消息
        if choice == "2":
            send_offline_msg.send_offlinemsg()
        #发送信息
        if choice == "3":
            send_message.send_message()
        #退出
        if choice == "4":
            break
    #关闭套接字
    close_socket()

if __name__ == "__main__":
    main()
