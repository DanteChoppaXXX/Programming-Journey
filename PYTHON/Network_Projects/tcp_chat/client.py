#!../env/bin/python3
import socket
import threading

#Connection Data
IP = "127.0.0.1"
PORT = 55555

#Choosing a Nickname
nickname = input("Choose a Nickname: ")

#Creating the client socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting the client to the Server
client.connect((IP, PORT))

def receive():
    keep_going = True
    while keep_going:
        try:
            #Receive Message from the Server
            #If 'NICK' send the client nickname
            message = client.recv(1024)
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message.decode())

        except (ConnectionError, ConnectionRefusedError):
            #CLose the connection when an error occur
            print("[X] An Error Occurred During Connection [X]")
            client.close()
            keep_going = False

def writing():
    keep_going = True
    while keep_going:
        try:
            #Sending data to the server
            message = f"{nickname}:{input(' ')}"
            client.send(message)

            #Receive data from the Server
            response = client.recv(1024)

            #Displaying the data received from the Server
            print(response.decode())

        except KeyboardInterrupt:
            #closing the client socket
            client.close()
            keep_going = False

#Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

writing_thread = threading.Thread(target=writing)
writing_thread.start()