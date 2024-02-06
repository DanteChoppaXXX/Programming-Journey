#!../../bin/python3
import socket

host = '54.81.67.241'
ports = [3306, 25, 22, 21]

# try:
#     for port in ports:
#         s = socket.socket()
#         s.connect((host, port))
#         answer = s.recv(1024)
#         print(answer)
#         s.close()
# except ConnectionRefusedError:
#     print('Firewall Active')
    
for port in ports:
    s = socket.socket()
    s.settimeout(7)
    try:
        s.connect((host, port))
        answer = s.recv(1024)
        print(f"Port {port} is Opened.\nThis is the banner for port {port}:\n", {answer})
        s.close()
    except (ConnectionRefusedError, socket.timeout):
        print(f"Port {port} is closed or filtered by a firewall!")
