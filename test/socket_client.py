import socket


def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.6.69',9999))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Machael',b'Tracy',b'Sarah']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()

if __name__ == '__main__':
    main()