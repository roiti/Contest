while 1:
	n,m = map(int,raw_input().split())
	if n == 0: break
	tsd = sorted([map(int,raw_input().split()) for i in range(m)])
	inf = [0]*n
	inf[0] = 1
	for t,s,d in tsd:
		if inf[s-1] == 1:
			inf[d-1] = 1
	print sum(inf)

