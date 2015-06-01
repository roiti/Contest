import sys,copy,itertools as it
sys.setrecursionlimit(10000)

dxy = zip([1,0,-1,0],[0,1,0,-1])
def check(A):
    if A[0] == _P[0][0] or A[-1] != c: return False
    for i in xrange(1,len(A)):
        if A[i-1] == A[i]: return False
    return True
    
def rec(x,y,b,c):
    P[y][x] = c
    for dx,dy in dxy:
        nx,ny = x+dx,y+dy
        if 0 <= nx < w and 0 <= ny < h and P[ny][nx] == b:
            rec(nx,ny,b,c)
    
while 1:
    h,w,c = map(int,raw_input().split())
    if h == 0: break
    _P = [map(int,raw_input().split()) for i in xrange(h)]

    ans = 0
    for change in it.product(range(1,7),repeat = 5):
        if not check(change): continue
        P = copy.deepcopy(_P)
        for c in change: rec(0,0,P[0][0],c)
        rec(0,0,P[0][0],0)
        ans = max(ans, sum(p.count(0) for p in P))

    print ans
    


