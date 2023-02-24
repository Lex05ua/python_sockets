# import socket library
import socket

# define the host and port of the server
host = 'localhost'
port = 8000

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client.connect((host, port))

while True:
    # send a message to the server
    message = input("Enter message: ")
    client.sendall(message.encode())

    # receive a response from the server
    response = client.recv(1024).decode()
    print(f"Received message from server: {response}")

sock.close()
