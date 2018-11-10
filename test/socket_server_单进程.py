import socket


def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local = s.bind(('192.168.6.69',9999))
    #让socket非阻塞
    s.setblocking(False)
    s.listen(100)
    client_data = []

    while True:
        try:
            client_socket,client_addr = s .accept()
        except:
            pass
        else:
            print("一个新的客户端到来...%s"%str(client_addr))
            client_socket.setblocking(False)
            client_data.append(client_socket,client_addr)

        for client_socket,client_addr in client_data:
            try:
                recv_data = client_socket.recv(1024)
            except:
                pass
            else:
                if len(recv_data) > 0:
                    print("recv_data:%s     client_addr:%s"%(recv_data,str(client_addr)))
                else:
                    client_socket.close()
                    client_data.remove(client_socket,client_addr)
                    print("%s已下线..."%str(client_addr))


if __name__ == '__main__':
    main()