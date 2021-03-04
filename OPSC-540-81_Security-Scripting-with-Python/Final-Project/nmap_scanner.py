'''
Michael Epstein
OPSC-540-81
'''
# import statements
import nmap3
import argparse
from datetime import datetime
import sys
import os
import io
import json
import ipaddress

#code

def host_file_scan(filename):
    #initates the nmap connection and builds the object nmap
    nmap = nmap3.Nmap()
    lines = open(filename, 'r').readlines()
    
    for line in lines:
        results = nmap.nmap_os_detection(line)
        results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
        open('nmap_scanner_output.txt', 'a').write(str(results))
        results = nmap.scan_top_ports(line)
        results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
        open('nmap_scanner_output.txt', 'a').write(str(results))
    
    #runs a few nmap scans on the hosts declared in your arguments and saves them to a file
    results = nmap.nmap_os_detection(filename)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open('nmap_scanner_output.txt', 'w').write(str(results))
    results = nmap.scan_top_ports(filename)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open('nmap_scanner_output.txt', 'a').write(str(results)) 

def host_scan(hostname):
    #initates the nmap connection and builds the object nmap
    nmap = nmap3.Nmap()
    
    #runs a few nmap scans on the hosts declared in your arguments and saves them to a file
    results = nmap.nmap_os_detection(hostname)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open('nmap_scanner_output.txt', 'w').write(str(results))
    results = nmap.scan_top_ports(hostname)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open('nmap_scanner_output.txt', 'a').write(str(results))    

def main():
    parser = argparse.ArgumentParser(description='Runs nmap scans against specified hostnames. Must be run with root permissions.')
    
    #allows only one argument to be specified
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f','--hostfile', help='File containing hosts', required=False)
    group.add_argument('-t','--hostname', help='insert a single hostname or IP', required=False)
    # create argparse dictionary
    args = vars(parser.parse_args())        
    print (args)
        
    if args['hostfile'] is not None:
        host_scan(args['hostname'])
    else:
        host_file_scan(args['hostfile'])
        
if __name__ == "__main__":
    main()
