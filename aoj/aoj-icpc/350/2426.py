import bisect
inf = 1e10
n,m = map(int,raw_input().split())
xy = [map(int,raw_input().split()) for i in range(n)]
X = sorted([i[0] for i in xy] + [-inf-1] + [inf+1])
Y = sorted([i[1] for i in xy] + [-inf-1] + [inf+1])

s = [[0]*(n+10) for i in range(n+10)]
for i in range(n):
	a = bisect.bisect_left(X,xy[i][0])
	b = bisect.bisect_left(Y,xy[i][1])
	s[a][b] += 1

for i in range(n+2):
	for j in range(n+2):
		s[i+1][j+1] += s[i+1][j] + s[i][j+1] - s[i][j]

for i in range(m):
	x1,y1,x2,y2 = map(int,raw_input().split())
	x1 = bisect.bisect_left(X,x1) - 1
	y1 = bisect.bisect_left(Y,y1) - 1
	x2 = bisect.bisect_left(X,x2+1) - 1
	y2 = bisect.bisect_left(Y,y2+1) - 1
	print s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]

