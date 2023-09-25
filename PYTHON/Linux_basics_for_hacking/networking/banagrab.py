#!../bin/python3
#Simple script for grabbing an application's banner

import socket

Host = "162.240.218.33"
Port = 21

s = socket.socket()
s.connect((Host, Port))
answer = s.recv(1024)

print(answer)
s.close