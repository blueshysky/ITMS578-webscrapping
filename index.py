from tkinter import *
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup

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
button = Button(bottomframe, text='UWU', fg='red', command='exit')
button.pack( side = "bottom")

TwButton = Button( centerframe, text="Twitter", fg='black', highlightcolor='blue')
TwButton.pack(side="right")

RdButton = Button( centerframe, text="Reddit", fg='black', highlightcolor='blue')
RdButton.pack(side="left")


Window.mainloop()

#grab url from a site
#url = 'https://www.google.com/'

#test to see if there is a respond
# respond = requests.get(url)
#print(respond)

#This step is to parse html to txt
# soup = BeautifulSoup(respond.text, "html.parser")

# print(soup.find_all('a'))

