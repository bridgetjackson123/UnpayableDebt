#given an individual url for NYT article, finds the content of the article
#cleans it and separates it into words

import requests
from bs4 import BeautifulSoup
import urllib

r = requests.get("https://www.nytimes.com/2017/01/19/opinion/a-diplomats-advice-for-the-trump-administration.html?rref=collection%2Ftimestopic%2FPuerto%20Rico&action=click&contentCollection=us&region=stream&module=stream_unit&version=latest&contentPlacement=4&pgtype=collection")
#http://www.nytimes.com/2016/12/28/opinion/a-zika-vaccine-but-for-whom.html")

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("p", {"class": "story-body-text story-content"})
time = soup.find_all("time", {"class": "dateline"})

#translator = str.maketrans('','', string.punctuation)
import string
for item in data:
	#print item.text this prints just the html text YAY	
	info = item.text
	info = info.lower()
	words = [x.strip(string.punctuation) for x in info.split()]
	print words
	print time[0].text
