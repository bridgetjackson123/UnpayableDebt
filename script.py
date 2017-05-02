from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('https://www.nytimes.com/topic/destination/puerto-rico').read()

soup = BeautifulSoup(r, "html.parser")

links = soup.find_all("a")

for link in links:
	#print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
	print link.get("href")
#print type(soup)
#print soup.prettify()[0:1000]
#letters = soup.find_all("li", class_="leaf")
#print type(letters)
#letters[0]
#prLinks = {}
#for element in letters:
#	prLinks[element.a.get_text()] = {}
#letters[0].a["href"]

#for link in soup.find_all('a'):
#	print(link.get('href'))



#import json

#with open("prLinks.json", "w") as writeJSON:
#	json.dump(prLinks, writeJSON)