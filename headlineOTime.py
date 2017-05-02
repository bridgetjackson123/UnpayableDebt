import csv
with open('titles.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        splitRow = row.split('\t')
        print splitRow[1]
        

"""from csv import reader
from matplotlib import pyplot

fo = open('titles.txt', 'r')
fr = fo.read()
fr = fr.split('\t')

titles = []
dates = []
for i in range(0, len(fr)):
	if(i%3 == 0):
		titles.append(fr[i])
		print fr[i]

#dates = [i[1] for i in data]
#print titles[0]

#pyplot.plot(range(len(dates)), dates)
#pyploy.show()
"""