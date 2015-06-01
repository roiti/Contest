while 1:
	n,m,a = map(int,raw_input().split())
	if n == 0: break
	amida = [[] for i in range(n)]
	for i in range(m):
		h,p,q = map(int,raw_input().split())
		amida[p-1].append([h,q])
		amida[q-1].append([h,p])
	for i in range(n):
		amida[i] = sorted(amida[i],reverse=True)
	y = 1001
	while 1:
		for i in range(len(amida[a-1])):
			if amida[a-1][i][0] < y:
				y = amida[a-1][i][0]
				a = amida[a-1][i][1]
				break
		else:
			break
	print a

