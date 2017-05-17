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


fo = open("prWords.txt", "w")
fop = open("prTotalTitles.txt", "w")

# Gets the first page and extracts the total numer of pages into num_of_pages
#word after q must be changed per query search


first_page = "https://www.nytimes.com/svc/collections/v1/publish/topics.nytimes.com/topic/destination/puerto-rico?page=0&dom=www.nytimes.com"
r = urllib.urlopen(first_page).read()
js = json.loads(r)
num_of_pages = int(js['members']['total_pages'])
count = 0

# For each page we get all articles and extract url and extract each word from each article and print as unicode object
for i in range (0,num_of_pages):	
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
					tText = title.encode('utf-8')
					#removes first title tag
					tText = tText[7:]
					titleAbrev = tText.rsplit('-', )[:-1]
					titleJoin = ''.join(titleAbrev)
					timeString = time["content"].encode('utf-8')
					timeString = timeString[:10]

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
							if wordString not in ["a", "about", "above", "above", "across", "after","afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]:
								fo.write("%s, " % (wordString.lower()))
								fo.write("%s, " % (timeString))	
								fo.write("%s \n" % (titleJoin))
								print wordString
								print timeString
								print titleJoin
					fop.write("%s, %s \n" % (titleJoin, timeString))
					print titleJoin
					print timeString
fo.close()
fop.close()