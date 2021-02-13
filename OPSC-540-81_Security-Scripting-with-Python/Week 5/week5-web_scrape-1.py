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

div_search = soup.find('div', id='info-for-menu')
div_search_tags = div_search.find_all('a')

for tags in div_search_tags:
    print(tags.prettify())

'''
Full XPath
/html/body/div[4]/header/div/div/nav/div/ul/li[5]/div
'''