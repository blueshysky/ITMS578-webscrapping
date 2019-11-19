from tkinter import *
from tkinter import messagebox
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup
import csv
#dependencies used if we were to access Twitter's API
    #import os
    #import tweepy as tw
    #import pandas as pd


#need to define functions inside the main loop and before the main gui to read
#defined reddit function
def redditFunction():
    # print("buttonclicked")

    #grab url from a site
    url = 'https://www.reddit.com/r/CasualConversation/comments/dxbvmi/i_got_a_raise_and_then_my_rent_went_up_anyone/'
    #test to see if there is a respond
    respond = requests.get(url)
    #print(respond)

    #This step is to parse html to txt
    soup = BeautifulSoup(respond.text, "html.parser")
    print(soup.find_all('svg'))
    soupVariable = (soup.find_all('svg'))
    messagebox.showinfo("Status", "Scanning completed")

def twitterFunction():
    



#make a window
Window = Tk()
Window.geometry("300x300")
Window.title("Webbsite")

#make a frame for the button
frame = Frame(Window)
frame.pack()

bottomframe = Frame(Window)
bottomframe.pack( side="bottom" )

centerframe = Frame(Window)
centerframe.place(relx=0.5, rely=0.5, anchor="center")
#positioning of the buttons
# relx=0.5, rely=0.5, anchor=CENTER)

#make a label
L1 = Label( Window, text="Welcome", fg='blue', bg='yellow', font=("arial", 16, "bold") ).pack()
#making buttons
button = Button(bottomframe, text='Exit', fg='red', command='exit')
button.pack( side = "bottom")

TwButton = Button( centerframe, text="Twitter", fg='white', highlightcolor='blue', command=twitterFunction)
TwButton.pack(side="right")

RdButton = Button( centerframe, text="Reddit", fg='white', highlightcolor='blue', command=redditFunction)
RdButton.pack(side="left")


Window.mainloop()








   
   





