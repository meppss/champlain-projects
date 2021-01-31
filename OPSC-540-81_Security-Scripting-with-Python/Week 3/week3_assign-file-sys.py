#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
'''
# import statements
import os
import argparse

def main():
    parser = argparse.ArgumentParser()\
    
    parser.add_argument("-f", help="Indent output")

    parser.add_argument("-u", help="User to search for in /etc/passwd file", action='append') # accept mult users
    parser.add_argument("--indent", help="Indent output")

    args = parser.parse_args()

if __name__ == "__main__":
    main()




## Part 1
# take arguments from the user
# parse and store these arguments in your program using argparse
# first argument the user will give your program will be an output file name
# open this file as a text file with write permissions
# second argument given by the user will be a username
# this argument can be entered multiple times for multiple user names

# Part 2
# executed with the proper arguments, your program will look up the operating system it is running on and first print out the OS name, release, and version
# next check if it is running on Linux or Unix
# if so, it will open and read through the lines of the /etc/passwd file and see if any of the provided usernames exist
# For any username found, that line will then be written to the output file provided by the user
# If the OS is something other than Linux/Unix, your program will state that the "OS is not supported" in a message to the user and the program will continue without checking the /etc/passwd file.

# Part 3
# After you have read through the contents of /etc/passwd, searched for each provided username, and then written results to the output file, close both files that you had open as you are done with them

# Part 4
# take as input() from the user a third file name.
# check if the file exists.  You can do this with either a call to exists() or try to open the file with a try/exception block which will catch if the file doesn't exist
# run a command using check_output() using the "shell=true" argument that will perform an "ls -l" on that file. run this and call check_output() two times as the input will contain a shell injection.
# first time you will run with the input entered directly and then the second time you will run it again only this time you need to escape characters to prevent the shell injection from working.  If you do this correctly, the first time the shell injection will work and the second time it won't.  HINT: You may need to catch an exception here to make sure your program exits gracefully.  Input from the user here will look something like: <inputfilename>;id

# example usage of program: my_week3_program.py -f outputfile.txt -u root -u shell