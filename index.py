import tkinter as tk
from tkinter import messagebox
import requests
import time
import urllib3.request
from bs4 import BeautifulSoup
import csv
#dependencies used if we were to access Twitter's API
import os
import tweepy as tw
import pandas as pd
from twitterscraper import query_tweets
import datetime as dt
#reddit api dependencies
import praw



#need to define functions inside the main loop and before the main gui to read
#defined reddit function
def redditFunction():
    # --had to scrap-- bueatiful soup functions and methods --had to scrap--
    # # print("buttonclicked")

    # #grab url from a site
    # url = 'https://www.reddit.com/r/CasualConversation/comments/dxbvmi/i_got_a_raise_and_then_my_rent_went_up_anyone/'
    # #test to see if there is a respond
    # respond = requests.get(url)
    # #print(respond)

    # #This step is to parse html to txt
    # soup = BeautifulSoup(respond.text, "html.parser")
    # mainbody = soup.find('div', class_="_1YCqQVO-9r-Up6QPB9H6_4 _1YCqQVO-9r-Up6QPB9H6_4")
    
    # for ptag in mainbody.find_all('a', class_="_23wugcdiaj44hdfugIAlnX "):
    #     print(ptag.text)  
    #--had to scrap-- bueatiful soup functions and methods --had to scrap--

    #declearing praw as a object to pass thru in secret passphrase but this is already connected to Vince's reddit account
    reddit = praw.Reddit(client_id='CsKw7Vf9lz8lEw',
                        client_secret='1EM41KrPCUllsfjjPDihLHX4EeE',
                        user_agent='webscrapper')
    #take the reddit object and call the function subreddit and assign it as a object 
    post = reddit.subreddit('CasualConversation')
    #hot method grab all "hot" topics of the subreddit
    hot = post.hot(limit=100)
    #this dictionary is made for the header of the csv file for the sake of colume organization
    dict = {"title":[], "subreddit":[], "score":[], "id":[], "url":[], "comms_num":[], "created":[], "body":[]}

    #for loop that goes thru the enitre dictionary and add information based on the catagory that is mined
    for submission in hot:
        dict["title"].append(submission.title)
        dict['subreddit'].append(submission.subreddit)
        dict["score"].append(submission.score)
        dict["id"].append(submission.id)
        dict["url"].append(submission.url)
        dict["comms_num"].append(submission.num_comments)
        dict["created"].append(submission.created)
        dict["body"].append(submission.selftext)

    #take the filled out dictionary and called the DataFrame class that use the data and parse it to csv
    rf = pd.DataFrame(dict)
    rf.to_csv(r'reddit.csv')
        
#twitter query, takes in a query of text written by the user and pass it thru
def twitterFunction(querytxt):
     date_begin=dt.date(2019,11,5)
     date_end=dt.date(2019,11,18)
     #the query tweet search the entire twitter for that query text  
     tweets = query_tweets(querytxt, 4000, date_begin, date_end, 4000, 'english')
     df = pd.DataFrame(t.__dict__ for t in tweets)
     df.to_csv(r'tweets.csv', index = None, header =True)

#Gui start up
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TopLevel_API (root)
    #GuI_support.init(root, top)
    root.mainloop()

#top part of the gui 
w = None
def create_TopLevel_API(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = TopLevel_API (w)
    #GuI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TopLevel_API():
    global w
    w.destroy()
    w = None

class TopLevel_API:
    #declearing the gui's window
    def __init__(self, top=None):
        '''defining color and background of the gui'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        #defining the dimension of the gui
        top.geometry("586x378+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Webscraping API")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        #created a top layer of the gui 
        self.qryTxt = tk.Text(top)
        self.qryTxt.place(relx=0.563, rely=0.476, relheight=0.116
                , relwidth=0.246)
        self.qryTxt.configure(background="white")
        self.qryTxt.configure(font="TkTextFont")
        self.qryTxt.configure(foreground="black")
        self.qryTxt.configure(highlightbackground="#d9d9d9")
        self.qryTxt.configure(highlightcolor="black")
        self.qryTxt.configure(insertbackground="black")
        self.qryTxt.configure(selectbackground="#c4c4c4")
        self.qryTxt.configure(selectforeground="black")
        self.qryTxt.configure(wrap="word")
        #inner button for eddit
        self.RdButton = tk.Button(top)
        self.RdButton.place(relx=0.085, rely=0.608, height=91, width=206)
        self.RdButton.configure(activebackground="#ececec")
        self.RdButton.configure(activeforeground="#000000")
        self.RdButton.configure(background="#ff80ff")
        self.RdButton.configure(disabledforeground="#a3a3a3")
        self.RdButton.configure(foreground="#ffffff")
        self.RdButton.configure(highlightbackground="#d9d9d9")
        self.RdButton.configure(highlightcolor="black")
        self.RdButton.configure(pady="0")
        self.RdButton.configure(text='''Reddit''')
        self.RdButton.configure(command= lambda: redditFunction()) #onclick reddit button launch the redditfunction 

        self.TwButton = tk.Button(top)
        self.TwButton.place(relx=0.085, rely=0.317, height=91, width=206)
        self.TwButton.configure(activebackground="#ececec")
        self.TwButton.configure(activeforeground="#000000")
        self.TwButton.configure(background="#ff80ff")
        self.TwButton.configure(disabledforeground="#a3a3a3")
        self.TwButton.configure(foreground="#ffffff")
        self.TwButton.configure(highlightbackground="#d9d9d9")
        self.TwButton.configure(highlightcolor="#000000")
        self.TwButton.configure(pady="0")
        self.TwButton.configure(text='''Twitter''')
        self.TwButton.configure(command= lambda: twitterFunction(self.qryTxt.get("0.0","end"))) #onclick twitter button launch the twitter function, with "qrytxt" parsing the input to string
        #label for asthetic
        self.lblWelcome = tk.Label(top)
        self.lblWelcome.place(relx=0.068, rely=0.053, height=76, width=492)
        self.lblWelcome.configure(activebackground="#f9f9f9")
        self.lblWelcome.configure(activeforeground="black")
        self.lblWelcome.configure(background="#f788d8")
        self.lblWelcome.configure(disabledforeground="#a3a3a3")
        self.lblWelcome.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.lblWelcome.configure(foreground="#ffffff")
        self.lblWelcome.configure(highlightbackground="#d9d9d9")
        self.lblWelcome.configure(highlightcolor="black")
        self.lblWelcome.configure(text='''ITMS-448: Webscraping API''')
        #exit button....what? yea that's all there is to it it close the program...
        self.exBtn = tk.Button(top)
        self.exBtn.place(relx=0.631, rely=0.741, height=33, width=76)
        self.exBtn.configure(activebackground="#ececec")
        self.exBtn.configure(activeforeground="#000000")
        self.exBtn.configure(background="#d9d9d9")
        self.exBtn.configure(disabledforeground="#a3a3a3")
        self.exBtn.configure(foreground="#000000")
        self.exBtn.configure(highlightbackground="#d9d9d9")
        self.exBtn.configure(highlightcolor="black")
        self.exBtn.configure(pady="0")
        self.exBtn.configure(text='''Exit''')
        self.exBtn.configure(command='exit')
        #label for asthetics
        self.TwLbl = tk.Label(top)
        self.TwLbl.place(relx=0.563, rely=0.344, height=40, width=145)
        self.TwLbl.configure(activebackground="#f9f9f9")
        self.TwLbl.configure(activeforeground="black")
        self.TwLbl.configure(background="#debef3")
        self.TwLbl.configure(borderwidth="4")
        self.TwLbl.configure(disabledforeground="#a3a3a3")
        self.TwLbl.configure(foreground="#ffffff")
        self.TwLbl.configure(highlightbackground="#d9d9d9")
        self.TwLbl.configure(highlightcolor="black")
        self.TwLbl.configure(text='''Twitter Query String:''')

    
#start the gui ....it's in the name!!!
if __name__ == '__main__':
    vp_start_gui()








   
   





