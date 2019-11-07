import requests
import time
import urllib3
from bs4 import BeautifulSoup

#grab url from a site
url = 'https://www.hackthissite.org/pages/index/index.php'

#test to see if there is a respond
respond = requests.get(url)
print(respond)

#This step is to 
#soup = BeautifulSoup(html_doc, 'html.parser')
# soup.findAll('a')