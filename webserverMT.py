#import socket module
from socket import *
import sys # In order to terminate the program
import threading

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
SERVER_PORT = 12007
serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(5)
print('Ready to serve...')

def client_handler(connectionSocket, addr):
    print("New Connection From Client At: ", addr[0], addr[1])
    print("HANDLED ON: ", threading.currentThread())

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP response into socket
        header = "HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\r\n\r\n" + outputdata + "\r\n"
        connectionSocket.send(header.encode())

        connectionSocket.close()
        print("Connection Closed from Client At: ", addr[0], addr[1])
    except IOError:
        #Send response message for file not found
        notFound = "HTTP/1.1 404 NotFound\r\n\r\n"
        connectionSocket.send(notFound.encode())
        
        #Close client socket
        connectionSocket.close()

while True:
    #Establish the connection
    try:
        connectionSocket, addr = serverSocket.accept()
        t = threading.Thread(target = client_handler, args = (connectionSocket, addr))
        t.start()
    except KeyboardInterrupt:
        serverSocket.close()   
             
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data