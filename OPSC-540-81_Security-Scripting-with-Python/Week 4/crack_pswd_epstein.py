import string
from hashlib import md5

hfd = open('hashes.txt', 'r') # open the file with hashes
afd = open('answers.txt', 'w') # open the file to write answers to

for hash in hfd.readlines():
    with open('/usr/share/john/password.lst') as wordlist:
      for word in wordlist.readlines():
          hash = hash.strip()
          pswd = word.strip() # use this var for writing to file
          pswd_bytes= pswd.encode('utf-8') # use this var for comparison against hash
          # write your code here

hfd.close()
afd.close()
