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
import subprocess
from os.path import basename

import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.application import MIMEApplication


#code

def host_file_scan(filename, scan_file):
    #initates the nmap connection and builds the object nmap
    nmap = nmap3.Nmap()
    lines = open(filename, 'r').readlines()
    
    for line in lines:
        results = nmap.nmap_os_detection(line)
        results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
        open(scan_file, 'a').write(str(results))
        results = nmap.scan_top_ports(line)
        results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
        open(scan_file, 'a').write(str(results))
    
    #runs a few nmap scans on the hosts declared in your arguments and saves them to a file
    results = nmap.nmap_os_detection(filename)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open(scan_file, 'w').write(str(results))
    results = nmap.scan_top_ports(filename)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open(scan_file, 'a').write(str(results))

     

def host_scan(hostname, scan_file):
    #initates the nmap connection and builds the object nmap
    nmap = nmap3.Nmap()
    
    #runs a few nmap scans on the hosts declared in your arguments and saves them to a file
    results = nmap.nmap_os_detection(hostname)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open(scan_file, 'w').write(str(results))
    results = nmap.scan_top_ports(hostname)
    results = json.dumps(results, indent=4, sort_keys=True, separators=(". ", "= "))
    open(scan_file, 'a').write(str(results))    


def email_send(scan_file):
    subject = "Nmap Scan Results"
    body = "This is an email containing an attachment sent from Python, used for Michael Epstein's Final Project in OPSC-540-81"
    sender_email = input("Type the email for the sender\n")
    receiver_email = input("Type the email for the recipient\n")
    password = input("Type your password and press enter:\n")
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    message.attach(MIMEText(body, 'plain')) # attach body text to part instance
    filename = scan_file  # In same directory as script
    attachment = open(filename, "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587) # initiates SMTP session for gmail.com
    server.starttls() # initiate TLS for security
    server.login(sender_email, password) #authentication
    text = message.as_string() #converts Multipart message into string value
    server.sendmail(sender_email, receiver_email, text) # send the email
    server.quit() # destroy the session

def main():
    parser = argparse.ArgumentParser(description='Runs nmap scans against specified hostnames. Must be run with root permissions.')
    
    #allows only one argument to be specified
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f','--hostfile', help='File containing hosts', required=False) # must be in same directory as script
    group.add_argument('-t','--hostname', help='insert a single hostname or IP', required=False)
   
    # create argparse dictionary
    args = vars(parser.parse_args())        
    print (args)
    
    scan_file = ("nmap_output" + str(datetime.now())+ ".txt") # file is created as part of host_file_scan() or host_scan()
    
    if args['hostfile'] is not None:
        host_file_scan(args['hostfile'], scan_file)
        email_send(scan_file)
    else:
        host_scan(args['hostname'], scan_file)
        email_send(scan_file)
        
    
if __name__ == "__main__":
    main()
    
    

