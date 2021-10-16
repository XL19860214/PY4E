# Copyright (c) Xuwei Li

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mySocket.send(cmd)

content = ''

while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    content += data.decode()
mySocket.close()

for line in content.split('\n'):
    for tag in ['Last-Modified', 'ETag', 'Content-Length', 'Cache-Control', 'Content-Type']:
        if tag in line:
            print(line) 

