
#    Nov 18, 2019 11:34:59 PM EST  platform: Windows NT

import sys

try:
    import tkinter as tk
    import requests
    import time
    import urllib3.request
    from bs4 import BeautifulSoup
    import csv
    import pandas as pd
    from twitterscraper import query_tweets
    import datetime as dt
    
except ImportError:
    import tkinter as tk
    import requests
    import time
    import urllib3.request
    from bs4 import BeautifulSoup
    import csv
    import pandas as pd
    from twitterscraper import query_tweets
    import datetime as dt
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GuI_support
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
def twitterFunction(querytxt):
     date_begin=dt.date(2019,11,5)
     date_end=dt.date(2019,11,18)
     
     tweets = query_tweets(querytxt, 4000, date_begin, date_end, 4000, 'english')
     df = pd.DataFrame(t.__dict__ for t in tweets)
     df.to_csv(r'tweets.csv', index = None, header =True)

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = TopLevel_API (root)
    GuI_support.init(root, top)
    root.mainloop()

w = None
def create_TopLevel_API(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = TopLevel_API (w)
    GuI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_TopLevel_API():
    global w
    w.destroy()
    w = None

class TopLevel_API:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("586x378+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Webscraping API")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

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
        self.RdButton.configure(command=redditFunction())

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
        self.TwButton.configure(command= lambda: twitterFunction(self.qryTxt.get("0.0","end")))

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

    

if __name__ == '__main__':
    vp_start_gui()


     