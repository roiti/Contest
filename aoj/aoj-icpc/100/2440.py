u = [raw_input() for i in range(input())]
t = [raw_input() for i in range(input())]
s = 1
for id in t:
	if id in u:
		print ("Opened" if s else "Closed") + " by " + id
		s = 1 - s
	else:
		print "Unknown",id

