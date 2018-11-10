import socket
import re
from multiprocessing import Process

HTML_ROOT_DIR = "../html"


class HTTPServer(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def start(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("[%s,%s]用户链接上了" % client_addr)
            handler_client_process = Process(target=self.handler_client, args=(client_socket,))
            handler_client_process.start()
            client_socket.close()

    def bind(self,host,port):
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def handler_client(self,client_socket):
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)
        request_line = request_data.splitlines()
        for line in request_line:
            print(line)
        request_start_line = request_line[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        if "/" == file_name:
            file_name = "/index.html"
        try:
            print("file_name:", HTML_ROOT_DIR + file_name)
            file = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 NOT FOUND\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found"
        else:
            file_data = file.read()
            file.close()
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = file_data.decode("utf-8")
        response = response_start_line + response_headers + "\r\n" + response_body
        print("response:", response)
        client_socket.send(bytes(response, "utf-8"))
        client_socket.close()


def main():
    httpServer = HTTPServer()
    httpServer.bind("192.168.6.69",9999)
    httpServer.start()


if __name__ == '__main__':
    main()