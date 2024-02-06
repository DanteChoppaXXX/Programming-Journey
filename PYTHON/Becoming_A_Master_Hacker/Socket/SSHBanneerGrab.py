#!../bin/python3
import socket

#IP = "192.168.122.145"
IP = input("Enter the IP ADDRESS: ")
PORT = 22

s = socket.socket()
s.connect((IP, PORT))

answer = s.recv(1024)

print(answer)

s.close()