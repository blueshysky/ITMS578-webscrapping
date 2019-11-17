#!/bin/bash
sudo apt update 
#sudo apt install python3 -y 

echo Installing pip, tkinter, requests, and bs4
sudo apt install python3-pip -y 
sudo apt-get install python3-tk -y 
sudo apt-get install python3-bs4 -y

sudo pip3 install requests 
sudo pip3 install BeautifulSoup4

