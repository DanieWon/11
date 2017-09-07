import send_online_msg
import feiQ_data


def send_message():
    """"发送信息"""
    msg = input("请输入消息")
    #content3 = "%d:%d:%s:%s:32:%s" % (version, int(time.time()), name, host_name, msg)
    willsend_content = send_online_msg.option(feiQ_data.chat, msg)
    #udp_socket.sendto(content3.encode("gbk"), aim_broadcast)
    send_online_msg.send_msg(willsend_content, feiQ_data.aim_broadcast)

