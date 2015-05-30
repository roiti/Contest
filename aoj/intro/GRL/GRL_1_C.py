V, E = map(int, raw_input().split())
G = [[float("inf")] * V for i in xrange(V)]
for i in xrange(V):
    G[i][i] = 0
for i in xrange(E):
    s, t, d = map(int, raw_input().split())
    G[s][t] = d

for k in xrange(V):
    for i in xrange(V):
        for j in xrange(V):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in xrange(V):
    if G[i][i] < 0:
        print "NEGATIVE CYCLE"
        exit()
    for j in xrange(V):
        if G[i][j] == float("inf"):
            G[i][j] = "INF"

for line in G:
    print " ".join(map(str, line))
