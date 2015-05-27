import sys
sys.setrecursionlimit(10000)
dxy = zip([1,0,-1,0],[0,1,0,-1])
def dfs(x,y,c):
    A[y][x]  = ord(c)
    res = False
    cnt = 0
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if 0 <= nx < m and 0 <= ny < n:
            if A[ny][nx] == c:
                res |= dfs(nx,ny,c)
            elif A[ny][nx] == ord(c):
                cnt += 1
    return res or cnt > 1
            
n,m = map(int,raw_input().split())
A = [list(raw_input()) for i in xrange(n)]
ans = False
for y in xrange(n):
    for x in xrange(m):
        if type(A[y][x]) is str:
            ans |= dfs(x,y,A[y][x])
print "Yes" if ans else "No"
