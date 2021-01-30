import argparse

parser = argparse.ArgumentParser()
parser.add_argument("interface", help="Interface", type=str)
parser.add_argument("port", help="Target Port", type=int)

args = parser.parse_args()

print("Using Network Interface: %s" % args.i)
print("Target Port: %d" % args.p)

args.i