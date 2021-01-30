'''
Michael Epstein
OPSC-540-81
'''

try:
  age = input("Enter your age: ")
  if(age > 21):
    print("You are over 21")
  else:
    print("You are under 21")
except Exception as error:
    print('ERROR: ',error)

  
'''
Output:
$ python3 week3-quiz-q3.py 
Enter your age: 12
ERROR:  '>' not supported between instances of 'str' and 'int'
'''