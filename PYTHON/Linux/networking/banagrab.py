#!../bin/python3
#Simple script for grabbing an application's banner

import socket

host = "93.188.163.64"
port = 22

socket = socket.socket()

socket.connect((host, port))

answer = socket.recv(1024)

print(answer)

socket.close
