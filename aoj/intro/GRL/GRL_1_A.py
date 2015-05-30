import heapq
from collections import namedtuple

edge = namedtuple("edge","to cost")

def dijkstra(G, s):
    que = [[0, s]]
    V = len(G)
    d = [float("inf")] * V
    d[s] = 0
    while que:
        c, v = heapq.heappop(que)
        if d[v] > c: continue
        for e in G[v]:
            if d[e.to] > d[v] + e.cost:
                d[e.to] = d[v] + e.cost
                heapq.heappush(que, [d[e.to], e.to])

    return d

V, E, r = map(int, raw_input().split())
G = [[] for i in xrange(V)]
for i in xrange(E):
    s, t, d = map(int, raw_input().split())
    G[s].append(edge(t, d))

d = dijkstra(G, r)
for i in d:
    if i < float("inf"):
        print i
    else:
        print "INF"
