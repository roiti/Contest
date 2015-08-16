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

N, Q = map(int, raw_input().split())
uf = UnionFind(N)
for loop in xrange(Q):
	p, a, b = map(int, raw_input().split())
	if p == 0:
		uf.unite(a, b)
	else:
		print "Yes" if uf.same(a, b) else "No"
