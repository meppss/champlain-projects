'''
Michael Epstein
OPSC-540-81
'''
# import statements
import argparse
from datetime import datetime
import getpass
#imports for parse_nmapxml
import xml.etree.ElementTree as etree
#imports for nessrest
import sys
sys.path.append('../')
from nessrest import ness6rest

#login credentials
scan = ness6rest.Scanner(url="https://nessusscanner:8834", login="username", password="password")

creds = [credentials.WindowsPassword(username="administrator", password="foobar"),
credentials.WindowsPassword(username="administrator", password="barfoo"),
credentials.SshPassword(username="nessususer", password="foobar")]


#build nessus scanner policy
scan.upload(upload_file="file.audit")
scan._policy_add_audit(category="Windows", filename="file.audit")
scan.policy_add(name="Scripted Scan", plugins="21156")

#launch scan
scan.scan_add(targets="192.168.0.1")
scan.scan_run()

# scan results
scan.scan_results()

#download KB for target
kbs = scan.download_kbs()

for hostname in kbs.keys():
    f = open(hostname, "w")
    f.write(kbs[hostname])
    f.close()


