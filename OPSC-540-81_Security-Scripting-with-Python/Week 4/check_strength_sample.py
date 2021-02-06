import string
import re

afd = open('answers.txt', 'r')

la = r"" # Please add your lower alpha re here
ua = r"" # Please add your upper alpha re here
n = r""  # Please add your number re here
sc = r"" # Please add your special character, ie !@#$%^&*() re here

for word in afd.readlines():
    pswd = word.strip()
    good_len =  False
    lower = False
    upper = False
    num = False
    special = False
    score = 0
    if False: # Please change this "False" statement to check for number of characters > 6
        good_len = True
        score += 1
    if re.search(la, pswd): # lowercase alpha search
        lower = True
        score += 1
    if re.search(ua, pswd): # upper alpha search
        upper = True
        score += 1
    if re.search(n, pswd):   # numbers search
        num = True
        score += 1
    if re.search(sc, pswd): # special characters
        special = True
        score += 1
    print("results for %s: score: %d" % (pswd,score))
    print("good_len: %s, lower: %s, upper: %s, num: %s, special: %s" % (good_len, lower, upper, num, special))
