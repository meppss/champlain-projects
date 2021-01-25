#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
Server Program
'''


import socket
import ssl

# SSL FILES

cert_file = 'server_cert.pem' # server cert (provided to client)
key_file = 'server_key.pem' # private ssl key

# code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, certfile='server_cert.pem', keyfile='server_key.pem', server_side=True)
s_ssl.bind(('localhost', 1234))
s_ssl.listen(5)


# Wait for connections
while True:
    try:  
        clientsocket, address = s_ssl.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    except Exception as e:
        print('{}: {}'.format(e.__class__.__name__, e))
