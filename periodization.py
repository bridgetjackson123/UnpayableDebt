foa = open("prWords5058.csv", "w")
fob = open("prWords5972.csv", "w")
foc = open("prWords7382.csv", "w")
fod = open("prWords8388.csv", "w")
foe = open("prWords8997.csv", "w")
fof = open("prWords9803.csv", "w")
fog = open("prWords0413.csv", "w")
foh = open("prWords1417.csv", "w")

for line in open("prTotalWords.csv", "r").readlines():
	lineInfo = line.split()
	date = lineInfo[1]
	year = date[:4]
	if(int(year) <= 1958):
		foa.write(line)
	elif(int(year) <= 1972):
		fob.write(line)
	elif(int(year) <= 1982):
		foc.write(line)
	elif(int(year) <= 1988):
		fod.write(line)
	elif(int(year) <= 1997):
		foe.write(line)
	elif(int(year) <= 2003):
		fof.write(line)
	elif(int(year) <= 2013):
		fog.write(line)
	elif(int(year) <= 2017):
		foh.write(line)

foa.close()
fob.close()
foc.close()
fod.close()
foe.close()
fof.close()
fog.close()
foh.close()