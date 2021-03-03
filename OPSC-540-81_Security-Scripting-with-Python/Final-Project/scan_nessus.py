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
scan = ness6rest.Scanner(url="https://local:8834", login="admin", password="Champlain!")

creds = [credentials.SshPassword(username="msfadmin", password="msfadmin")]


#build nessus scanner policy
scan.upload(upload_file="CIS_Ubuntu_18.04_LTS_Server_v2.0.1_L1.audit")
scan._policy_add_audit(category="Linux", filename="CIS_Ubuntu_18.04_LTS_Server_v2.0.1_L1.audit")
scan.policy_add(name="Scripted Scan", plugins="21156")

#launch scan
scan.scan_add(targets="192.168.1.3")
scan.scan_run()

# scan results
scan.scan_results()

#download KB for target
kbs = scan.download_kbs()

for hostname in kbs.keys():
    f = open(hostname, "w")
    f.write(kbs[hostname])
    f.close()