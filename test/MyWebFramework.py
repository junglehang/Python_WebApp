import time
from test.MyWebServer import HTTPServer


class Application(object):


    def __init__(self,urls):
        self.urls = urls


    def __call__(self, env, start_response):
        path = env.get("PATH_INFO","/")
        for url,handler in self.urls:
            if path == url:
                return handler(env,start_response)
        status = "404 not found"
        headers = []
        start_response(status,headers)
        return "not found"

def show_time(env,start_response):
    status = "200 OK"
    headers = [
        ("Content-Type","text/plain")
    ]
    start_response(status,headers)
    return time.ctime()

def show_hello(env,start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello boy"

def show_haha(env,start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello haha"

def show_byby(env,start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "boy byby"


def main():
    urls = [
        ("/", show_time),
        ("/ctime",show_time),
        ("/sayhello",show_hello),
        ("/saybyby",show_byby)
    ]
    app = Application(urls)
    http_server = HTTPServer(app)
    http_server.bind("192.168.6.69",9999)
    http_server.start()

if __name__ == '__main__':
    main()