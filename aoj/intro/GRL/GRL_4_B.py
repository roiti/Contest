def tsort(G):
    def bfs(s):
        que = [s]
        used[s] = True
        while que:
            u = que.pop(0)
            res.append(u)

            for v in G[u]:
                indeg[v] -= 1
                if indeg[v] == 0 and not used[v]:
                    used[v] = True
                    que.append(v)

    indeg = [0] * V
    used = [False] * V
    res = []
    for u in xrange(V):
        for v in G[u]:
            indeg[v] += 1
    for u in xrange(V):
        if indeg[u] == 0 and not used[u]:
            bfs(u)
    return res


V, E = map(int, raw_input().split())
G = [[] for i in xrange(V)]
for i in xrange(E):
    s, t = map(int, raw_input().split())
    G[s].append(t)

ans = tsort(G)
for i in ans:
    print i
