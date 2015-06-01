while 1:
	n,m = map(int,raw_input().split())
	if n == 0: break
	EBY = [raw_input().split() for i in range(n)]
	EBY = [[e,int(y)-int(b),int(y)] for e,b,y in EBY]
	for i in range(m):
		year = int(raw_input())
		for j in range(n):
			if EBY[j][1] < year <= EBY[j][2]:
				print EBY[j][0], year-EBY[j][1]
				break
		else:
			print "Unknown"

