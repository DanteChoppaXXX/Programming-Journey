#!../../bin/python3
#Port Scanner

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 port_scanner.py <ip>')

#Add a pretty banner
print('_' * 50)
print()
print(f'Scanning Target: {target}')
print('Time Started:',datetime.now())
print('_' * 50)
print()

ports = [21, 22, 25, 53, 80, 443, 3306]
try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(3)
        result = s.connect_ex((target, port))
        #answer = s.recv(1024)
        if result == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed or filtered')
        s.close()
except KeyboardInterrupt:
    print('Exiting Program.')
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()
except socket.error:
    print('Could not connect to server.')
    sys.exit()
