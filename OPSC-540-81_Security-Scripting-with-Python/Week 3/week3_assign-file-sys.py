#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
'''
# import statements
import os
import platform
import argparse
import subprocess
import shlex

def main():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", help="Type the name of the intended output file") # accept file name
    parser.add_argument("-u", help="User to search for in /etc/passwd file", nargs='?', action='append', type=str) # accept mult users
    parser.add_argument("-q", help="type name of file to be found") # accept file name


    args = parser.parse_args()
    
    print('OS Name: ', detect_os())
    print("OS Release: ", platform.release())
    print('OS Version: ', platform.version())

    if detect_os() == 'Windows':
        print('OS is not supported')
        return
    elif detect_os() == 'Linux' or 'Unix':
        for u in args.u:
            with open(args.f, 'w') as note:
                try:
                    note.write(subprocess.check_output(["grep %s /etc/passwd" % u], shell=True).decode('utf-8'))
                    note.close()
                except Exception:
                    print('No value found for', u)
    else:
        return
    
    print('Name of file to check for existence: ')
    lum = input()
    print ("File exists:", str(os.path.exists(lum)))
    try:
        subprocess.check_output(["ls -l %s;id" % lum], shell=True).decode('utf-8')
        subprocess.check_output(["ls -l %s;id" % lum], shell=True).decode('utf-8')
    except Exception:
        print('No file found')
                
def detect_os():
    detected_os = platform.system()
    return detected_os
if __name__ == "__main__":
    main()