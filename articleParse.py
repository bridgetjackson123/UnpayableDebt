#given an individual url for NYT article, finds the content of the article
#cleans it and separates it into words

import requests
from bs4 import BeautifulSoup
import urllib

r = requests.get("http://www.nytimes.com/2016/12/28/opinion/a-zika-vaccine-but-for-whom.html")
#http://www.nytimes.com/2016/12/28/opinion/a-zika-vaccine-but-for-whom.html")

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("p", {"class": "story-body-text story-content"})

#translator = str.maketrans('','', string.punctuation)
import string
for item in data:
	#print item.text this prints just the html text YAY	
	info = item.text
	info = info.lower()
	words = [x.strip(string.punctuation) for x in info.split()]
	print words
