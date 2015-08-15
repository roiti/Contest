import sys
sys.setrecursionlimit(100010)
def dfs(s,d):
    global circle
    for t in G[s]:
        if dist[t] == -1:
            dist[t] = d+1
            dfs(t,d+1)
        if d-dist[t] > 1:
            circle = d-dist[t]+1
 
n = int(raw_input())
G = [[] for i in xrange(n)]
for loop in xrange(n):
    a,b = map(int,raw_input().split())
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)
 
dist = [-1]*n
dist[0] = 0
circle = 0
dfs(0,0)
 
if circle == n:
    if n%2 == 0:
        print 2,n
    else:
        print 2,n-1
else:
    if circle%2 == 0:
        print 1,n
    else:
        print 1,n-1
