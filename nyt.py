import json
import urllib
import requests
from bs4 import BeautifulSoup


# Gets the first page and extracts the total numer of pages into num_of_pages
first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q=debt&sort=relevance&page=1&dom=www.nytimes.com"
r = urllib.urlopen(first_page).read()
js = json.loads(r)
num_of_pages = int(js['members']['total_pages'])
count = 0

# For each page we get all articles and extract url
#for i in range (1,num_of_pages):	
#	url = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q=debt&sort=relevance&page="+str(i)+"&dom=www.nytimes.com"
#	r = urllib.urlopen(url).read()
#	js = json.loads(r)
#	num_of_items = len(js['members']['items'])
#	for item in range(1,num_of_items):
#		print js['members']['items'][item]['url']

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

		#translator = str.maketrans('','', string.punctuation)
		import string
		for item in data:
			#print item.text this prints just the html text YAY	
			info = item.text
			info = info.lower()
			words = [x.strip(string.punctuation) for x in info.split()]
			for j in range(0, len(words)):
				print words[j].encode('utf-8')
				print time[0].text

