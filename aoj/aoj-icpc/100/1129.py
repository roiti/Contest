while 1:
	n,r = map(int,raw_input().split())
	if n == 0: break
	card = range(n,0,-1)
	for i in range(r):
		p,c = map(int,raw_input().split())
		card = card[p-1:p-1+c] + card[:p-1] + card[p-1+c:]
	print card[0]

