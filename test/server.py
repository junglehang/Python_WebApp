from wsgiref.simple_server import make_server
from test.hello import application

def main():
    httpd = make_server('',8000,application)
    print("SerVing Http on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    main()