#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
Server Program
'''

# import required modules
from socket import socket, AF_INET, SOCK_STREAM
import ssl
import sys

# SSL FILES

key_file = 'server_key.pem' # private ssl key
cert_file = 'server_cert.pem' # server cert (provided to client)

# code

def echo_client(rx):
    while True:
        data = rx.recv(8192)
        if data == b'':
            break
        rx.send(data)
    rx.close()
    print('Connection closed')


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)

    # Wrap with an SSL layer requiring client certs
    s_ssl = ssl.wrap_socket(s,
                            keyfile=key_file,
                            certfile=cert_file,
                            server_side=True
                            )
    # Wait for connections
    while True:
        try:
            c_socket,c_addr = s_ssl.accept()
            print('Got connection', c_socket, c_addr)
            echo_client(c_socket)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))
    echo_server(('', 20000))
    