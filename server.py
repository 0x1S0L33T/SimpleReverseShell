import socket
import sys

# Create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 1337
        s = socket.socket()
    except socket.error as msg:
        print("Something went wrong" + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Port Binded: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Something went wrong (Binding)+ str(msg)" + "\n" + "Retrying...")
        bind_socket()

# Establish connection with a client (socket must be listening)

def socket_accept():
    conn,address = s.accept()
    print("Connection has bin established! And that's a great news ;)"
    + "IP: " + address[0] + "Port: " + str(address[1]))
    send_command(conn)
    conn.close()

# Send command to the client
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        # Encode the command and don't do anything if command is empty
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()