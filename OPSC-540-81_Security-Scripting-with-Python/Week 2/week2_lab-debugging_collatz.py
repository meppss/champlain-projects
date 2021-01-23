#!/usr/bin/python3

'''
Michael Epstein
OPSC-540-81
'''

# import statements
import sys

# code
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
def check_number(number):    
    even_result = is_even(number)
    if even_result == True:
        number = number // 2     
        return number
    else:
        number = 3 * number + 1
        return number
def collatz(number):    
    while number != 1:        
        # print(number)        
        number = check_number(number)    
        print("Final number is: " + str(number))
    
    
if __name__ == "__main__":    
    try:
        number = int(input("Enter a number:"))    
        collatz(number)
    except (TypeError, ValueError):
        print("Please re-run and enter an Integer")
    except:
        print("Unexpected error:", sys.exc_info())