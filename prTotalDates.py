import json
import urllib
import requests
import sys
from bs4 import BeautifulSoup
import string

from datetime import datetime

def removePunc(word):
	wordString = word
	wordString = wordString.translate(None, '-\'!@#$%\",.?!')
	#wordString = wordString.replace('\"', '')
	return wordString


fo = open("prTotalDates.txt", "w")

# Gets the first page and extracts the total numer of pages into num_of_pages
#word after q must be changed per query search


first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?page=0&dom=www.nytimes.com"
#first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q=puerto-rico&sort=relevance&page=1&dom=www.nytimes.com"
r = urllib.urlopen(first_page).read()
js = json.loads(r)
num_of_pages = int(js['members']['total_pages'])
count = 0

# For each page we get all articles and extract url and extract each word from each article and print as unicode object
for i in range (0,num_of_pages):	
	#url = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q=puerto-rico&sort=relevance&page="+str(i)+"&dom=www.nytimes.com"
	print i
	url = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?page="+str(i)+"&dom=www.nytimes.com"
	r = urllib.urlopen(url).read()
	js = json.loads(r)
	num_of_items = len(js['members']['items'])
	for item in range(0,num_of_items):
		r = requests.get(js['members']['items'][item]['url'])
		soup = BeautifulSoup(r.content, "html.parser")

		data = soup.find_all("p", {"class": "story-body-text story-content"})
		articleType = soup.find("meta", {"name":"PT"})
		if(articleType is not None):
			if(articleType["content"].lower() == 'article'):
				#time = soup.find_all("time", {"class": "dateline"})
				time = soup.find("meta", {"itemprop":"dateModified"})
				if(time is not None):
					
					title = soup.find('title')
					print title
					tText = title.encode('utf-8')
					#removes first title tag
					tText = tText[7:]
					returnMe = tText.rsplit('-', )[:-1]
					returnMeJoin = ''.join(returnMe)
					timeString = time["content"].encode('utf-8')
					timeString = timeString[:10]
					print timeString
					fo.write("%s \n " % (timeString))	
fo.close()