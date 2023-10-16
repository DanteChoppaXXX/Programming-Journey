#!../../bin/python3
import socket

TCP_IP = '192.168.0.108'
TCP_PORT = 2023
BUFFER_SIZE = 100

#Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

conn, addr = s.accept()
print('Connection address:', addr)

while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        break
    print('Received data:', data)
    conn.send(data) #echo
conn.close()