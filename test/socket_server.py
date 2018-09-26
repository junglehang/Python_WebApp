import socket
import time
import threading



def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('192.168.6.69',9999))
    s.listen(5)
    print("Waiting for connection")
    while True:
        sock,addr = s.accept()
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()


def tcplink(sock,addr):
    print("Accept connection from %s:%s"%addr)
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s'%addr)


if __name__ == "__main__":
    main()