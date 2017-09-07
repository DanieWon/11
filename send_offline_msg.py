import feiQ_data
import send_online_msg


def send_offlinemsg():
    """发送离线消息"""
    #content2 = "%d:%d:%s:%s:%d:%s" % (version, int(time.time()), name, host_name, offline, content)
    willsend_content = send_online_msg.option(feiQ_data.offline, feiQ_data.content)
    #udp_socket.sendto(content2.encode("gbk"), aim_broadcast)
    send_online_msg.send_msg(willsend_content, feiQ_data.aim_broadcast)


