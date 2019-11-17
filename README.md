# ITMS 478-578 Final Project  

The objective of this github repository is to develop a simple webscrapping program to get data from Reddit and Twitter and post it into a .csv file.

## create-env.sh  

This script is written so that all the necessary python dependencies and imports will automatically be installed  
to run the `` .py `` file with ease. This script should both work on Ubuntu and Windows environments that have the  
Linux bash shell. 

```
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
```
requests and beautifulsoup4 for parsing  
numpy, pandas, and tweepy for working with the Twitter API  
