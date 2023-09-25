#!../bin/python3
import socket

HOST = "0.0.0.0"
PORT = 2033
BUFFER_SIZE = 100

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

connect, addr = sock.accept()
print("Connection address: ", addr)

while 1:

    data=connect.recv(BUFFER_SIZE)
    if not data:break
    print("Received data:", data)
    connect.send(data) #echo
    connect.close
