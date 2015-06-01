while 1:
	N = input()
	if N == 0: break
	M = [map(int,raw_input().split()) for i in range(N+1)]
	K = set(M[-1][1:])
	a = -1
	for i in range(N):
		if set(M[i][1:]) >= K:
			if a != -1:
				a = -1
				break
			a = i + 1
	print a

