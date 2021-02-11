#!/usr/bin/python3

import re
from fqdn import FQDN

def check_ip(ip_val):
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_val):
        return print(ip_val, "is a valid IP")
    else:
        return print(ip_val, "is an invalid IP")
        
def check_fqdn(fqdn_val):
    fqdn_val = FQDN(fqdn_val)
    if fqdn_val.is_valid == 'True':
        return print(fqdn_val, 'is a valid FQDN') 
    else:
        return print(fqdn_val, 'is an invalid FQDN') 
        
def main():
    ip_input = input("Enter either a good or bad IP address: ")
    fqdn_input = input("Enter a good or bad FQDN name: ")
    check_ip(ip_input)
    check_fqdn(fqdn_input)

if __name__ == "__main__":
    main()