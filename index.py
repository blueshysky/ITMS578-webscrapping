from tkinter import *
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup

import os
import tweepy as tw
import pandas as pd



#grab url from a site
url = 'https://www.reddit.com/r/CasualConversation/comments/dxbvmi/i_got_a_raise_and_then_my_rent_went_up_anyone/'
#test to see if there is a respond
respond = requests.get(url)
print(respond)

#This step is to parse html to txt
soup = BeautifulSoup(respond.text, "html.parser")

print(soup.find_all('a'))



