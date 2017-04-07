from collections import defaultdict
class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.par = range(size)

    def find(self, x):
        if x == self.par[x]: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return

        if (self.rank[x] > self.rank[y]):
            self.par[y] = x
        else:
            self.par[x] = y
            if (self.rank[x] == self.rank[y]): self.rank[y] += 1

N, K, L = map(int, raw_input().split())
pq = [map(int, raw_input().split()) for i in xrange(K)]
rs = [map(int, raw_input().split()) for i in xrange(L)]

road = UnionFind(N)
rail = UnionFind(N)
for p, q in pq:
    road.unite(p - 1, q - 1)
for r, s in rs:
    rail.unite(r - 1, s - 1)

for i in xrange(N):
    road.find(i)
    rail.find(i)

pair = defaultdict(int) 
for i, j in zip(road.par, rail.par):
    pair[i, j] += 1

print " ".join(map(str, [pair[road.par[i], rail.par[i]] for i in xrange(N)]))
