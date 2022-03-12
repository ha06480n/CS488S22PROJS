import socket
import sys
import time

if(len(sys.argv) != 4): # Incorrect number of arguments
    print("Error: missing or additional arguments")
    quit()

host = str(sys.argv[1])  # The server's hostname or IP address
port = int(sys.argv[2])  # The port used by the server
myTime = int(sys.argv[3]) # The duration in seconds for which data is generated

host = socket.gethostbyname(host)
if((port < 1024) or (port > 65535)): # Port out of range
    print("Error: port number must be in the range 1024 to 65535")
    quit()

address = (host, port)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP socket
clientSocket.connect(address)
message = bytearray(1000) #Message 1000 bytes long of 0
counter = 0 #Counter for number of messages sent

timeStart = time.perf_counter()
while timeStart - time.perf_counter() < myTime:
    clientSocket.send(message)
    counter += 1
    continue

print("sent=", counter, " KB rate=", counter*8.0/10000.0, " Mbps")
clientSocket.close()