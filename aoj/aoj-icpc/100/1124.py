while 1:
	N,Q = map(int,raw_input().split())
	if N == 0: break
	C = [0]*100
	for _ in range(N):
		D = map(int,raw_input().split())
		for i in D[1:]:
			C[i] += 1
	print C.index(max(C)) if max(C) >= Q else 0

