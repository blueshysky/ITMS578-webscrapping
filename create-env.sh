#!/bin/bash
sudo apt update 
#sudo apt install python3 -y [for ubuntu]
echo Installing pip, tkinter, requests, and bs4
sudo apt install python3-pip -y 
sudo apt-get install python3-tk -y 
sudo apt-get install python3-bs4 -y
sudo apt-get install python3-tweepy -y

#python2 install for windows environments
pip install tweepy
pip install requests 
pip install BeautifulSoup4
pip install numpy
pip install pandas

#python3
pip3 install tweepy
pip3 install requests 
pip3 install BeautifulSoup4
pip3 install numpy
pip3 install pandas
pip3 install praw

#resources
#https://www.earthdatascience.org/courses/earth-analytics-python/using-apis-natural-language-processing-twitter/get-and-use-twitter-data-in-python/
