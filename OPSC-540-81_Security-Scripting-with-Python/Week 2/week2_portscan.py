#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
'''

# import required modules
from socket import *
import sys
from datetime import datetime as dt
import ipaddress
import argparse

# code
ports = [20, 21, 22, 23, 80, 443, 513]

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ipaddr")
args = parser.parse_args()
try:
    host_ip = ipaddress.ip_address(args.ipaddr)
except ValueError:
    sys.exit("Bad IP Address entered")

t1 = dt.now()
print("Scan started:", t1)
print("\n")
try:
    for port in ports:
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(0.8)
        result = s.connect_ex((str(host_ip), port))
        if result == 0:
            print("[OPEN]:", port)
        else:
            print("[CLOSED]:", port)
        s.close()
except KeyboardInterrupt:
    print("User stopped script.")
    sys.exit()

except Exception as e:
    print(e)
    sys.exit()

t2 = dt.now()
print("\n")
print("Scan ended:", t1)
total = (t2-t1)
print("Scan finished in", total)
