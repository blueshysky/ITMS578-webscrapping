from tkinter import *
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup



#grab url from a site
url = 'https://www.google.com/'
#test to see if there is a respond
respond = requests.get(url)
print(respond)

#This step is to parse html to txt
soup = BeautifulSoup(respond.text, "html.parser")

print(soup.find_all('a'))



