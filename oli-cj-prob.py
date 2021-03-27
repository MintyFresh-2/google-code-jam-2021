
def cjfunction (cj,jc,instring):

	pattern = list(instring)
	newstring = ""
	cost = 0

	for el in range (0,len(pattern)):
		if pattern[el] == "?":
			pattern[el]=""
		newstring +=(pattern[el])

	for x in range (0,len(newstring)-1):
		if newstring[x] == "C" and newstring[x+1] == "J":
			cost+= cj
		elif newstring[x] == "J" and newstring[x+1] == "C":
			cost+= jc

	return cost



numbertest = int(input ())
for case in range (0, numbertest):
	testcase = input().split(" ")
	casecost = cjfunction(int(testcase[0]),int(testcase[1]),testcase[2])
	print("Case #"+str(case+1)+": "+str(casecost))
