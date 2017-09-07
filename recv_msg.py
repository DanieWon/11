import socket
import feiQ_data
import send_online_msg


def deal_msg(recv_data_):
    """处理消息数据"""
    _recv_data = recv_data_.decode("gbk", errors = "ignore")
    message_list = _recv_data.split(":", 5)
    #用字典保存数据信息
    msg_dict = dict()
    msg_dict["version"] = message_list[0]
    msg_dict["packet_numb"] = message_list[1]
    msg_dict["user_name"] = message_list[2]
    msg_dict["host_name"] = message_list[3]
    msg_dict["command"] = message_list[4]
    msg_dict["content"] = message_list[5]
    return msg_dict

def deal_data(command_):
    """获取数据command的十六进制前六位和后两位"""
    recv_command = int(command_) & 0x000000ff
    additional_function = int(command_) & 0xffffff00
    return recv_command, additional_function


def receive_message():
    """接收数据并根据数据反馈"""
    while True:
        recv_data, aim_broadcast = feiQ_data.udp_socket.recvfrom(1024)
        feiq_data = deal_msg(recv_data)
        command, command_option = deal_data(feiq_data["command"])
        if command == feiQ_data.IPMSG_BR_ENTRY:
            print("用户上线", aim_broadcast, "用户名", feiq_data["user_name"])
        elif command == feiQ_data.IPMSG_BR_EXIT:
            print("用户离线", aim_broadcast, "用户名", feiq_data["user_name"])
        elif command == feiQ_data.IPMSG_SENDMSG:
            print("收到消息：", aim_broadcast, "信息", feiq_data["content"] )
            msg = send_online_msg.option(feiQ_data.IPMSG_RECVMSG)
            send_online_msg.send_msg(msg, aim_broadcast)
