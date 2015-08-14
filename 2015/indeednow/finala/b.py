inf = 10**9
drc = [zip([1,-1,1,-1,0,0],[0,0,-1,-1,1,-1]),
       zip([1,-1,1,-1,0,0],[0,0,1,1,1,-1])]
R,C = map(int,raw_input().split())
a = [list(raw_input()) for i in xrange(R)]
for r in xrange(R):
    for c in xrange(C):
        if a[r][c] == "s":
            sr,sc = r,c
            a[r][c] = 0
        if a[r][c] == "t":
            gr,gc = r,c
            a[r][c] = 0
a = [map(int,ai) for ai in a]
 
cost = [[inf]*C for i in xrange(R)]
cost[sr][sc] = 0
que = [[sr,sc,0]]
while que:
    r,c,d = que.pop(0)
    if cost[r][c] < d: continue
    for dr,dc in drc[r%2]:
        nr,nc = r+dr,c+dc
        if 0 <= nr < R and 0 <= nc < C and d+a[nr][nc] < cost[nr][nc]:
            cost[nr][nc] = d+a[nr][nc]
            que.append([nr,nc,d+a[nr][nc]])
print cost[gr][gc]
