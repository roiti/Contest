S = sorted([[i,j] for i in range(1,100) for j in range(i+1,151)], key = lambda x:x[0]**2+x[1]**2)
while 1:
	h,w = map(int,raw_input().split())
	if h == 0: break
	hi,wi = S[S.index([h,w])+1]
	print hi,wi

