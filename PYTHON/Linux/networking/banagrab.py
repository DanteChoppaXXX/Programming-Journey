#!../bin/python3
#Simple script for grabbing an application's banner

import socket

host = "93.188.163.64"
Ports = [587,9100]

for i in range (0,5):

    socket = socket.socket()

    Ports = Ports[i]

    print("This is the banner for the Port")

    print(Ports)

    socket.connect((host, Ports))

    answer = socket.recv(1024)

    print(answer)

    socket.close()
