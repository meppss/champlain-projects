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

def get_inputs():
    # create argparse arguments
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
    # return 'Scan Started: <SCAN_ID>' if started scan. Otherwise pass error message.

def wait_email_user():
    # wait for email from nessus stating the scan is complete. 
    # when this email is received, email the completed nessus scan document.
    # return email sent verification or error message

def read_results():
    # read report, if any highs or criticals are found, state the number of each within the email to the user.

def main():
    # retrieve inputs from get_inputs()
    # pass inputs to nessus_start_scan()
    # while loop on wait_email_user() to send the completed report to user when the Nessus scan is completed.
    # print email sent verification or error message from wait_email_user() 

if __name__ == "__main__":
    main()







