from tkinter import *
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup

#make a window
Window = Tk()
Window.geometry("300x300")
Window.title("Webbsite")

#make a label
L1 = Label( Window, text="Welcome", fg='blue', bg='yellow', font=("arial", 16, "bold") ).pack()

Window.mainloop()

#grab url from a site
#url = 'https://www.google.com/'

#test to see if there is a respond
# respond = requests.get(url)
#print(respond)

#This step is to parse html to txt
# soup = BeautifulSoup(respond.text, "html.parser")

# print(soup.find_all('a'))

