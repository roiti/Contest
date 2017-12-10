import sys
sys.setrecursionlimit(10000)
def getpar(i):
    for j in edge[i]:
        if par[j] == -1:
            par[j] = i
            getpar(j)

V = int(raw_input())
edge = [[] for i in xrange(V)]
par = [-1] * V
par[0] = 0
for loop in xrange(V - 1):
    A, B = map(int, raw_input().split())
    edge[A].append(B)
    edge[B].append(A)

getpar(0)

visit = [False] * V
visit[0] = True
N = int(raw_input())
for loop in xrange(N):
    P = int(raw_input())
    while not visit[P]:
        visit[P] = True
        P = par[P]

print (sum(visit) - 1)* 2
