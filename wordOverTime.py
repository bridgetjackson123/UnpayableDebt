
searchWord = raw_input('Search word one: ')

fileName = raw_input('Output file name: ')
fo = open(fileName, 'w')
#wordFormat = ''.join((searchWord, ','))

for line in open('prTotalWords.csv', 'r').readlines():
	lineInfo = line.split()
	word = lineInfo[0]

	if(word == searchWord):
		print word
		#lineWithoutWord = ''.join(lineInfo[:1])
		#fo.write('%s\n' % (str(lineInfo)))
		fo.write(line[len(searchWord):])

fo.close()