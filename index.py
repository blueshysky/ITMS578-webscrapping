from tkinter import *
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup
import csv

#dependencies used if we were to access Twitter's API
    #import os
    #import tweepy as tw
    #import pandas as pd



#grab url from a site
url = 'https://www.reddit.com/r/CasualConversation/comments/dxbvmi/i_got_a_raise_and_then_my_rent_went_up_anyone/'
#test to see if there is a respond
respond = requests.get(url)
#print(respond)

#This step is to parse html to txt
soup = BeautifulSoup(respond.text, "html.parser")
print(soup.find_all('svg'))
#  soupVariable = (soup.find_all('svg'))


#trying to write the output from [print(soup.find_all('svg'))] into a csv file 
with open('output.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    #print(soup.find_all('svg'))
    #for row in csv_reader:
    #    if line_count == 0:
    #        print(f'Column names are {", ".join(row)}')
    #        line_count += 1
    #    print(soup.find_all('svg'))
    #    line_count += 1
   
   
   





