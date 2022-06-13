# import socket module
from socket import *
import sys


SERVER_ADDRESS = ('', 13000)
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverSocket.bind(SERVER_ADDRESS)
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message =  connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode("UTF-8"))
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode("UTF-8"))
        connectionSocket.send('\r\n'.encode("UTF-8"))
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not found\r\n\r\n'.encode("UTF-8"))
        connectionSocket.send('<html><head></head><body><h1>404 Not found</h1></body></html>\r\n'.encode("UTF-8"))
        connectionSocket.close()
        break
    # Close client socket
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
