#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
'''
# import statements
import os

def read_logs():
    # open file
    logs = '/var/log/messages'
    with open(logs, 'r') as stuff:
        print('File Path: ' + os.path.abspath(logs))
        #read file
        for lines in (stuff.readlines()[-50:]):
            if 'NIC' in lines:   
                print(lines, end ='')


if __name__ == "__main__":
    read_logs()
