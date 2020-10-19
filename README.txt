Ayush Parikh
asparikh
112228873

For the program, the server must be run first so that it can listen to and accept incoming connections. Next, to run the client, 3 arguments must be provided - 
server IP address/host name, server port number (which must be 12007), and the filename. The client will then create a socket and 
connect to the specified port number at the IP address/host. If the connection is not successful, the client socket will close. Otherwise, the client will 
create a GET request for the specified filename and send it over to the server. The server in the meantime has created a thread to deal with this connection 
and then once the GET message is received, it will parse the message, get the file and send that back to the client, which will then display the contents of the 
file. If the client wants to request another file, the 3 arguments must be provided again with the desired filename. Connection is closed through keyboard
interruption or if an error occurred during this entire process. 