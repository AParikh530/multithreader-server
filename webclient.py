import sys
from socket import *

def run_client(server_name, server_port, filename):
    client_socket = socket(AF_INET, SOCK_STREAM)
    try:
        client_socket.connect((server_name, server_port))
        header = "GET /" + filename + " HTTP/1.1\r\n\r\n"
        client_socket.send(header.encode())
        header_response = client_socket.recv(2000)
        print("FROM SERVER: " + header_response.decode())
        client_socket.close()
    except:
        client_socket.close()


if __name__ == "__main__":
    sn = sys.argv[1]
    sp = int(sys.argv[2])
    sf = sys.argv[3]
    run_client(sn, sp, sf)