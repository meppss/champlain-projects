'''
Michael Epstein
OPSC-540-81
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="Interface", type=str)
parser.add_argument("port", help="Target Port", type=int)
parser.add_argument("ip_address", help="Target IP Address", type=str)

args = parser.parse_args()

print("Using Network Interface: %s" % args.interface)
print("Target Port: %d" % args.port)
print("IP Address: %s" % args.ip_address)


'''
Output:
$ python3 week3-quiz-q1.py 5 1 192.168.1.1
Using Network Interface: 5
Target Port: 1
'''