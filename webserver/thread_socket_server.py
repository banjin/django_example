#!/usr/bin/env python

import socket
import errno
import threading
import time


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = "say hello, <h1>welcome<h2> from {thread_name}"


response_params = [
    'HTTP/1.1 200 OK',
    'Date: Fir, 7 July 2019 17:30:28 GMT',
    'Content-Type: html/plain, charset=utf-8',
    'Content-Length: {length}\r\n',
    body
]

response = '\r\n'.join(response_params)


def handle_connect(conn, addr):
    """处理连接
    """
    request = b''
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)


    print(request)
    
    conn.send(response.encode())
    conn.close()


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用,保证我们每次按ctrl+c后能够快速重启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)
    print("http://127.0.0.1:8000")

    try:
        while True:
            conn, addr = serversocket.accept()
            handle_connect(conn, addr)
    finally:
        serversocket.close()


if __name__ == "__main__":
    main()

