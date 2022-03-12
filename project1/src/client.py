# Import libraries
import socket

# Create server
ServerName = 'localhost'
ServerPort = 1200
ServerAddress = (ServerName, ServerPort)

# Create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket

# Ask for connection to server
clientSocket.connect(ServerAddress)

# three-way handshake is performed
# a TCP connection is established between the client and server.
while 1:

    # Create message
    message = input('Enter the lower case message: ')

    # Send message
    clientSocket.send(message.encode("utf-8"))

    # Receive from server
    modified_sent = clientSocket.recvfrom(2048)

    # Print received message
    print("From server:", modified_sent)

    continue

# Close connection
clientSocket.close()
