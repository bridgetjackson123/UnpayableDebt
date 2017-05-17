import json
import urllib
import requests
import sys
from bs4 import BeautifulSoup
import string

from datetime import datetime

def dateTimeFormat(s):
	month = s[0].lower()
	if(month[:3] == 'upd'):
		month = s[1].lower()
		dayYear = '/'.join(s[2:])
	elif(month[0].isdigit()):
		month = '12'
		dayYear = '12/1912'
		dateTimeString = month + '/' + dayYear
		return dateTimeString
	elif len(s) > 4:
		dayYear = '/'.join(s[1:-2])
	elif len(s) == 2:
		dayYear = '/'.join(s[1:])
	else:
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


fo = open("titlesOnly.txt", "a")


# Gets the first page and extracts the total numer of pages into num_of_pages
#word after q must be changed per query search
keywords = []
keywords.append('debt')
keywords.append('crisis')
keywords.append('hedge-funds')
keywords.append('shortage')
keywords.append('financial-crisis')
keywords.append('restructuring')

for kword in keywords:
	searchword = kword
	print searchword
	first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q="+searchword+"&sort=relevance&page=1&dom=www.nytimes.com"
	r = urllib.urlopen(first_page).read()
	js = json.loads(r)
	num_of_pages = int(js['members']['total_pages'])
	count = 0

	# For each page we get all articles and extract url and extract each word from each article and print as unicode object
	for i in range (1,num_of_pages):	
		url = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?q="+searchword+"&sort=relevance&page="+str(i)+"&dom=www.nytimes.com"
		
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
			returnMe = tText.rsplit('-', )[:-1]
			returnMeJoin = ''.join(returnMe)
			#print returnMeJoin
			if(len(time) == 0):
				timeString = '00-00-0000'
			else:
				timeString = time[0].text
				timeString = [x.strip(string.punctuation) for x in timeString.split()]
				print timeString
				dTime = dateTimeFormat(timeString)	
				datetime_object = datetime.strptime(dTime, '%m/%d/%Y').date()
				source = 'NYT'
				#timeObject = datetime_object
				print dTime
				#fo.write("%s \t " % (datetime_object))
				#fo.write("%s \n" % (returnMeJoin))
				fo.write("%s \n" % (returnMeJoin))
					
fo.close()