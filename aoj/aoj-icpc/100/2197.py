while 1:
	n = input()
	if n == 0: break
	ans = 0
	for i in range(1,n/2+1): 
		s = i
		for j in range(i+1,n/2+2):
			s += j
			if s >= n:
				if s == n:
					ans += 1
				break
	print ans

