import socket
import feiQ_data
import time


def option(stat, message=""):
    """设置发送的内容"""
    content = "%d:%d:%s:%s:%d:%s" % (feiQ_data.version, int(time.time()), feiQ_data.name, feiQ_data.host_name, stat, message)
    return content


def send_msg(send_data, send_broadcast):
    """发送"""
    feiQ_data.udp_socket.sendto(send_data.encode("gbk"), send_broadcast)


def send_onlinemsg():
    """发送上线消息"""
    #content1 = "%d:%d:%s:%s:%d:%s" % (version, int(time.time()), name, host_name, online, content)
    willsend_content = option(feiQ_data.online, feiQ_data.content)
    #udp_socket.sendto(content1.encode("gbk"), aim_broadcast)
    send_msg(willsend_content, feiQ_data.aim_broadcast)


