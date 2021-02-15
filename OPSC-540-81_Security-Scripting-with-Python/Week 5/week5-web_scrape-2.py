#!/usr/bin/python3
'''
Michael Epstein
OPSC-540-81
'''

#import statements
import urllib.request
from bs4 import BeautifulSoup

#open webpage and save to variable
f = urllib.request.urlopen("https://www.champlain.edu/current-students") 

#create BeautifulSoup object
soup = BeautifulSoup(f,'html.parser')

div_search = soup.find('div', class_='student-login')
div_search_user = div_search.find(id='login-username')
div_search_pass = div_search.find(id='login-password')

print(div_search_user)
print(div_search_pass)

'''
Full XPath
/html/body/div[4]/div[4]/section/form/div[1]
'''