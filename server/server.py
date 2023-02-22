# import socket library
import socket

# define the host and port to listen on
host = 'localhost'
port = 8000

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific host and port
server.bind((host, port))

# listen for incoming connections
server.listen(1)

while True:
    # wait for a client to connect
    print('Waiting for a client to connect...')
    conn, addr = server.accept()
    print(f"Connection from {addr}, {conn}")

    while True:
        # receive data from the client
        data = conn.recv(1024).decode()
        
        # if no any data 
        if not data:
            print("Client left")
            break
        
        print(f"Received message from client: {data}")

        # send a response back to the client
        response = input("Enter response: ")
        conn.sendall(response.encode())

    # close the connection
    conn.close()
