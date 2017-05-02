import json
import urllib
import requests
import sys
from bs4 import BeautifulSoup
import string
fo = open("dbInfoCredit.txt", "w")


# Gets the first page and extracts the total numer of pages into num_of_pages
#word after q must be changed per query search
first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q=credit&sort=relevance&page=1&dom=www.nytimes.com"
r = urllib.urlopen(first_page).read()
js = json.loads(r)
num_of_pages = int(js['members']['total_pages'])
count = 0

# For each page we get all articles and extract url and extract each word from each article and print as unicode object
for i in range (1,num_of_pages):	
	url = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q=debt&sort=relevance&page="+str(i)+"&dom=www.nytimes.com"
	
	r = urllib.urlopen(url).read()
	js = json.loads(r)
	num_of_items = len(js['members']['items'])
	for item in range(1,num_of_items):
		r = requests.get(js['members']['items'][item]['url'])
		soup = BeautifulSoup(r.content, "html.parser")

		data = soup.find_all("p", {"class": "story-body-text story-content"})
		
		time = soup.find_all("time", {"class": "dateline"})

		title = soup.find('title')

		#translator = str.maketrans('','', string.punctuation)
		for word in data:
			#print word.text -- this prints just the html text 
			info = word.text
			info.lower()
			#words = [x.translate(None, '!@#$%\",.?!') for x in info.split()]
			words = [x.strip(string.punctuation) for x in info.split()]
			for j in range(0, len(words)):
				#prints individual word, lower case, stripped of punctuation as string
				wordString = words[j].encode('utf-8')
				wordStrin = wordString.translate(None, '!@#$%\",.?!')
				print wordStrin
				#prints time stamp as string
				timeString = time[0].text
				source = 'NYT'
				
				#insertString = wordString + timeString 
				fo.write("%s\t" % (wordString))
				fo.write("%s \t %s \t %d \n" % (timeString, source, j))
				
fo.close()
