import socket
import re
import sys
from multiprocessing import Process

HTML_ROOT_DIR = "../html"
WSGI_PYTHON_DIR = "../wsgipython"


class HTTPServer(object):
    def __init__(self,app):
        self.app = app
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

    def start_response(self,status,headers):
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n"%header
        self.response_headers = response_headers

    def handler_client(self,client_socket):
        request_data = client_socket.recv(1024)
        print("request_data:", request_data)
        request_line = request_data.splitlines()
        for line in request_line:
            print(line)
        request_start_line = request_line[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        method = re.match(r"(\w+) +/[^ ]* ",request_start_line.decode("utf-8")).group(1)
        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        response = self.response_headers + "\r\n" + response_body
        print("response:", response)
        client_socket.send(bytes(response, "utf-8"))
        client_socket.close()



def main():
    sys.path.insert(1,WSGI_PYTHON_DIR)
    httpServer = HTTPServer()
    httpServer.bind("192.168.6.69",9999)
    httpServer.start()


if __name__ == '__main__':
    main()