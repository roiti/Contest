dx,dy = [-1,0,1,0],[0,-1,0,1]
while 1:
	N = input()
	if N == 0: break
	x,y = [0]*N,[0]*N
	for i in range(1,N):
		n,d = map(int,raw_input().split())
		x[i] = x[n]+dx[d]
		y[i] = y[n]+dy[d]
	print max(x)-min(x)+1,max(y)-min(y)+1

