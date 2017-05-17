import json
import urllib
import requests
import sys
from bs4 import BeautifulSoup
import string

from datetime import datetime

def dateTimeFormat(s):
	month = s[0].lower()
	dayYear = '/'.join(s[1:])

	if(month[:3] == 'jan'):
		month = '01'
	elif(month[:3] == 'feb'):
		month = '02'
	elif(month[:3] == 'mar'):
		month = '03'
	elif(month[:3] == 'apr'):
		month = '04'
	elif(month[:3] == 'may'):
		month = '05'
	elif(month[:3] == 'jun'):
		month = '06'
	elif(month[:3] == 'jul'):
		month = '07'
	elif(month[:3] == 'aug'):
		month = '08'
	elif(month[:3] == 'sep'):
		month = '09'
	elif(month[:3] == 'oct'):
		month = '10'
	elif(month[:3] == 'nov'):
		month = '11'
	else:
		month = '12'
	dateTimeString = month + '/' + dayYear

	return dateTimeString

def removePunc(word):
	wordString = word
	wordString = wordString.translate(None, '-\'!@#$%\",.?!')
	#wordString = wordString.replace('\"', '')
	return wordString


fo = open("articleWords.txt", "a")


# Gets the first page and extracts the total numer of pages into num_of_pages
#word after q must be changed per query search
keywords = []
keywords.append('debt')
keywords.append('crisis')
keywords.append('hedge-funds')
keywords.append('shortage')
keywords.append('financial-crisis')
keywords.append('restructuring')
keywords.append('responsibility')
keywords.append('')
for kword in keywords:

	searchword = kword
	first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q="+searchword +"&sort=relevance&page=1&dom=www.nytimes.com"
	r = urllib.urlopen(first_page).read()
	js = json.loads(r)
	num_of_pages = int(js['members']['total_pages'])
	count = 0

	# For each page we get all articles and extract url and extract each word from each article and print as unicode object
	for i in range (1,num_of_pages):	
		url = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q="+searchword +"&sort=relevance&page="+str(i)+"&dom=www.nytimes.com"
		
		r = urllib.urlopen(url).read()
		js = json.loads(r)
		num_of_items = len(js['members']['items'])
		for item in range(1,num_of_items):
			r = requests.get(js['members']['items'][item]['url'])
				
			soup = BeautifulSoup(r.content, "html.parser")

			data = soup.find_all("p", {"class": "story-body-text story-content"})
			
			time = soup.find_all("time", {"class": "dateline"})

			title = soup.find('title')
			tText = title.encode('utf-8')
			#removes first title tag
			tText = tText[7:]
			tSplit = tText.rsplit('-', )[:-1]
			tJoin = ''.join(tSplit)
			for word in data:
				#print word.text -- this prints just the html text 
				info = word.text
				info.lower()
				#words = [x.strip(string.punctuation) for x in info.split()]
				words = info.split()
				for j in range(0, len(words)):
					#prints individual word, lower case, stripped of punctuation as string
					wordString = words[j].encode('utf-8')

					wordString = removePunc(str(wordString.lower()))
					#prints time stamp as string
					timeString = time[0].text
					timeString = [x.strip(string.punctuation) for x in timeString.split()]
					
					dTime = dateTimeFormat(timeString)	
					datetime_object = datetime.strptime(dTime, '%m/%d/%Y').date()
					source = 'NYT'
					fo.write("%s\n" % (wordString.lower()))
					fo.write("%s\t %s \t %d \t %s \n" % (datetime_object, source, j, tJoin))
				
fo.close()
