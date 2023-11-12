#!../env/bin/python3
import socket
import threading

#Connection Data
IP = "0.0.0.0"
PORT = 55555

#Creating the socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding the socket to the Connection Data
server.bind((IP, PORT))

#Listen for incoming connections
server.listen(5)
print(f"[*] Listening For Incoming Connections [*]")
#Lists for storing clients and their nicknames
clients = []
nicknames = []

#Sending messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

#Handling messages from the clients
def handle(client):
    keep_going = True
    while(keep_going):
        try:
            #Broadcating messages to connected clients
            message = client.recv(1024)
            broadcast(message)
        except:
            #Removing and Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left!".encode('utf-8'))
            nicknames.remove(nickname)
            keep_going = False

#Receiving / Listening Function
def receive():
    while True:
        #Accept Connection
        client, address = server.accept()
        print(f"[*] Connected with {address}")

        #Request and store nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        #Print and broadcast the nickname
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the server!".encode('utf-8'))
        client.send(b"Connected To The Server!")

        #Start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()