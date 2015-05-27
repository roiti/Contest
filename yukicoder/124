import sys
sys.setrecursionlimit(100000)

dxy = zip([1,0,-1,0],[0,1,0,-1])

def isKadomatsu(a,b,c):
    if a == 0 or b == 0: return True
    return b < a < c or b < c < a or a < c < b or c < a < b

W,H = map(int,raw_input().split())
M = [map(int,raw_input().split()) for i in xrange(H)]
que = [[0,0,0]]
cost = [[[-1]*W for i in xrange(H)] for j in xrange(10)]
cost[0][0][0] = 0

while que:
    w,h,bef = que.pop(0)
    if (w,h) == (W-1,H-1):
        print cost[bef][h][w]
        break
    cur = M[h][w]
    for dx,dy in dxy:
        nw,nh = w+dx,h+dy
        if not (0 <= nw < W and 0 <= nh < H): continue
        aft = M[nh][nw]
        if not isKadomatsu(bef, cur, aft): continue
        if cost[cur][nh][nw] != -1: continue
        cost[cur][nh][nw] = cost[bef][h][w]+1
        que.append([nw,nh,cur])
else:
    print -1
