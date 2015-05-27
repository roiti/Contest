from collections import deque
inf = 10**12
def dist(i,j):
    x1,y1 = XY[i]
    x2,y2 = XY[j]
    d = (x1-x2)**2+(y1-y2)**2
    if d-int(d**0.5)**2 > 0:
        return int(d**0.5)/10*10+10
    else:
        if int(d**0.5)%10 == 0:
            return int(d**0.5)
        else:
            return int(d**0.5)/10*10+10

N = int(raw_input())
XY = [map(int,raw_input().split()) for i in xrange(N)]
D = [[dist(i,j) for i in xrange(N)] for j in xrange(N)]
ans = inf
que = deque([[0,0]])
maxd = [inf]*N
maxd[0] = 0
while que:
    i,d = que.popleft()
    if d >= ans:
        continue
    if i == N-1:
        ans = min(ans,d)
        continue
    for j in xrange(N):
        if i == j: continue
        if D[i][j] < maxd[j] and d < maxd[j]:
            maxd[j] = max(d,D[i][j])
            que.append([j,maxd[j]])
print ans
