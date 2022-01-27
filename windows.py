import socket
import threading

hostserver ='target ip'
hostclient='my ip'
portserver=6677
portclient=7766
buffer = 2048
backlog = 5
message=''
data=''

def server():
    while True:
        global data
        global message
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
            addr = (hostserver, portserver)
            sock.connect(addr)
            message = str(input('my pc : '))
            sock.sendall(message.encode('UTF-8'))
            sock.close() 
        except Exception as e:
            print(e)
    

def client():
    while True:
        global data
        global message
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
            client_address = (hostclient, portclient)
            sock.bind(client_address)
            sock.listen(backlog)
            server, address = sock.accept()
            data = server.recv(buffer)
            if data:
                print('\n target pc : '+ str(data))
                sock.close()
        except Exception as e:
            print(e)
    

chser=threading.Thread(target=server)
chcli=threading.Thread(target=client)
chser.start()
chcli.start()

