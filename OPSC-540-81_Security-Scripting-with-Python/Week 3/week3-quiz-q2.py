'''
Michael Epstein
OPSC-540-81
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Number to add", nargs='+')
parser.add_argument("--indent", help="Indent output")

args = parser.parse_args()

num_nums = len(args.n)
print("Adding %d numbers." % num_nums)
sum = 0
for n in range(0, num_nums):
    sum = sum + int(args.n[n])

if (args.n):
    print("\tSum = %d" % sum)
else:
    print("Sum = %s" % sum)
    
'''
Output:
$ python3 week3-quiz-q2.py -n 5 1 2 2 2 2 2 2 2
Adding 9 numbers.
        Sum = 20
'''