#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
Server Program
'''

import socket
import ssl


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_ssl = ssl.wrap_socket(s, ca_certs = 'server_cert.pem')
s_ssl.connect(('localhost', 1234))
s_ssl = s_ssl.recv(1024)
print(s_ssl.decode("utf-8"))
