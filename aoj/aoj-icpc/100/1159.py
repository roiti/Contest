while 1:
	n,p = map(int,raw_input().split())
	if n == 0: break
	have = [0]*n
	cup = p
	i = 0
	while 1:
		if cup > 0:
			have[i] += 1
			cup -= 1
			if have[i] == p:
				break
		else:
			cup += have[i]
			have[i] = 0
		i = (i+1)%n
	print i

