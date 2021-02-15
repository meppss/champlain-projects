#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
'''

#import statements
import argparse
import ipaddress
import nessrest
import nmap
import sys
import gmail
import time

def get_inputs():
    # create argparse arguments, -i for cmd-line args; -f for input file.
    # check for cmd-line arguments, if present skip input file
    # check for input file
    # use cmd-line args or input file to identify IPs/CIDR
    # check IPs are in the correct format
    # return IPs/CIDR to main()

def nessus_scan_start(input)
    # use input as IPs or CIDRs for scan.
    # Use default network scan as template, mark it to send email on completion. 
    # use input in place for hosts, start scan.
    # When scan is finished, email to user that scan is complete.
    # return 'Scan Started: ', <SCAN_ID>. if started scan. Otherwise pass error message.

def wait_email_user():
    # wait for email from nessus stating the scan is complete. 
    # use gmail library to check for email every 15 seconds.
    # when this email is received, return True to main()
    # return email sent verification or error message

def read_results(scan_id):
    # search nessus using scan_id
    # read scan report, if any highs or criticals are found, state the number of each within the email to the user.
    # return number of highs/mediums to main()

def email_user():
    # email scan report to user via nessus
    # Nessus has already been preconfigured with an access key to gmail.
    # print email_sent confirmation.

def main():
    # retrieve inputs from get_inputs()
    inputs = get_inputs()
    # pass inputs to nessus_start_scan()
    scan_id = nessus_scan_start(inputs)
    # while loop on wait_email_user(), when True is received break while loop.
    while wait_email_user() == False:
        time.sleep(15)            
    # read_results(scan_id) and pass the scan_id to search nessus for. Save result to variable as dictionary
    read_results(scan_id)
    # run email_user(scan_id) and pass in the scan_id. 
    email_user(scan_id)

if __name__ == "__main__":
    main()







