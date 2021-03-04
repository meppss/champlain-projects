'''
Michael Epstein
OPSC-540-81
'''
# import statements
import argparse
from datetime import datetime
import getpass
import xml.etree.ElementTree as etree
import sys
sys.path.append('../')
import os
import io
from nessrest import ness6rest


def init_scan(args):
    #login credentials

    scan = ness6rest.Scanner(url='https://localhost:8834',login='admin',password='Champlain!', insecure=True)
    targets = nmap_xml_parse(args['nmap_file'])
    scan.upload(args['nmap_file'])
    filename = scan.res[u'fileuploaded']
    scan.policy_exists(args['policy'])
    scan.policy_set(args['policy'])
    settings = {"settings": {}}
    settings["settings"].update({"import_nmap_xml":"yes"}) 
    settings["settings"].update({"import_nmap_xml_file":filename})
    scan.action(action="policies/" + str(scan.policy_id), method="put",extra=settings)
    scan.policy_set(args['policy'])
    t = ','
    targets = t.join(nmap_xml_parse(args['nmap_file']))
    print (targets)
    scan.scan_add(targets=targets,name=args['scanname'])
    scan.scan_run()
    
    
def nmap_xml_parse(filename):
    # parse nmap xml, find hosts
    tree_root = etree.parse(filename)
    nmap_run = tree_root.getroot()
    hosts = nmap_run.findall('host')
    targets = []
    for host in hosts:
        ipaddr = host.find('address')
        targets.append(ipaddr.attrib['addr'])
    return(targets)

def export_scanresult():
    file_format = 'csv'  # options: nessus, csv, db, html
    dbpasswd = ''

    scan = ness6rest.Scanner(url="https://localhost:8834", login="admin", password="Champlain!", insecure=True)

    scan.action(action='scans', method='get')
    folders = scan.res['folders']
    scans = scan.res['scans']

    if scan:
        scan.action(action='scans', method='get')
        folders = scan.res['folders']
        scans = scan.res['scans']

        for f in folders:
            if not os.path.exists(f['name']):
                if not f['type'] == 'trash':
                    os.mkdir(f['name'])

        for s in scans:
            scan.scan_name = s['name']
            scan.scan_id = s['id']
            folder_name = next(f['name'] for f in folders if f['id'] == s['folder_id'])
            folder_type = next(f['type'] for f in folders if f['id'] == s['folder_id'])

            # Ignore trashed scans
            if folder_type == 'trash':
                continue

            if s['status'] == 'completed':
                file_name = '%s_%s.%s' % (scan.scan_name, scan.scan_id, file_format)
                file_name = file_name.replace('\\','_')
                file_name = file_name.replace('/','_')
                file_name = file_name.strip()
                relative_path_name = folder_name + '/' + file_name
                # PDF not yet supported
                # python API wrapper nessrest returns the PDF as a string object instead of a byte object, making writing and correctly encoding the file a chore...
                # other formats can be written out in text mode
                file_modes = 'wb'
                # DB is binary mode
                #if args.format == "db":
                #  file_modes = 'wb'
                with io.open(relative_path_name, file_modes) as fp:
                    if file_format != "db":
                        fp.write(scan.download_scan(export_format=file_format))
                    else:
                        fp.write(scan.download_scan(export_format=file_format, dbpasswd=dbpasswd))

def main():    
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-f','--nmap_file', help='file generated with nmap -oX', required=True)
    parser.add_argument('-n','--scanname', help='name for the scan in nessus', required=False, default="scripted-scan")
    parser.add_argument('-P','--policy', help='Nessus policy that is prepared already within Nessus, default is "scripted-scan_$datetime.now()"')
    parser.add_argument('-p','--password', help='password for logging in to nessus server', required=False)
    parser.add_argument('-u','--user', help='username for logging in to nessus server', required=False)
    
    args = vars(parser.parse_args())
    
    print (args)
    policy
    if not args['user']:
        args['user'] = getpass._raw_input('User: ')
    if not args['password']:
        args['password'] = getpass.getpass()
    if not args['scanname']:
        args['scanname'] = "scripted-scan_%s"%datetime.now().strftime("%Y%m%d-%H%M%S")
    print (args)
    
    #scan usually takes about 10-15 minutes
    init_scan(args)
    
    
    

if __name__ == "__main__":
    main()
    


'''
#login credentials
scan = ness6rest.Scanner(url="https://local:8834", login="admin", password="Champlain!")

creds = [credentials.SshPassword(username="kali", password="kali")]


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
    '''