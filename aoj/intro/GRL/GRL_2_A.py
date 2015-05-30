class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.par = range(size)
        self.g_num = size

    def find(self, x):
        if x == self.par[x]: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return

        self.g_num -= 1
        if (self.rank[x] > self.rank[y]):
            self.par[y] = x
        else:
            self.par[x] = y
            if (self.rank[x] == self.rank[y]): self.rank[y] += 1

    def group_num(self):
        return self.g_num



V, E = map(int, raw_input().split())
es = [map(int, raw_input().split()) for i in xrange(E)]
es.sort(key = lambda x: x[2])

uf = UnionFind(V)
ans = 0
for e in es:
    if not uf.same(e[0], e[1]):
        uf.unite(e[0], e[1])
        ans += e[2]
print ans
