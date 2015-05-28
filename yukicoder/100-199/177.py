class MaxFlowDinic:
    class edge:
        def __init__(self, to, rev, cap):
            self.to, self.rev, self.cap = to, rev, cap

    def __init__(self, v):
        self.V = v
        self.G = [[] for i in xrange(self.V)]

    def add(self, frm, to, cap):
        self.G[frm].append(self.edge(to, len(self.G[to]), cap))
        self.G[to].append(self.edge(frm, len(self.G[frm]) - 1, 0))

    def add_dual(self, frm, to, cap):
        self.G[frm].append(self.edge(to, len(self.G[to]), cap))
        self.G[to].append(self.edge(frm, len(self.G[frm]) - 1, cap))

    def bfs(self, s):
        self.level = [-1] * self.V
        self.level[s] = 0
        que = []
        que.append(s)
        while (que):
            v = que.pop(0)
            for i in xrange(len(self.G[v])):
                e = self.G[v][i];
                if e.cap > 0 and self.level[e.to] < 0:
                    self.level[e.to] = self.level[v] + 1;
                    que.append(e.to)


    def dfs(self, v, t, f):
        if v == t: return f
        for i in xrange(self.itr[v], len(self.G[v])):
            self.itr[v] = i
            e = self.G[v][i]
            if e.cap > 0 and self.level[v] < self.level[e.to]:
                d = self.dfs(e.to, t, min(f, e.cap))
                if d > 0:
                    e.cap -= d
                    self.G[e.to][e.rev].cap += d
                    return d
        return 0

    def max_flow(self, s, t):
        inf = float("inf")
        flow = 0
        while 1:
            self.bfs(s)
            if self.level[t] < 0: return flow

            self.itr = [0] * self.V
            f = self.dfs(s, t, inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, inf)


W, N = int(raw_input()), int(raw_input())
J = map(int, raw_input().split())
M = int(raw_input())
C = map(int, raw_input().split())

mf = MaxFlowDinic(201)

for i in xrange(N):
    mf.add(0, i + 1, J[i])

for i in xrange(M):
    mf.add(100 + i, 200, C[i])

NG = [[False] * M for i in xrange(N)]
for i in xrange(M):
    QX = map(int, raw_input().split())
    for j in QX[1:]:
        NG[j - 1][i] = True
    for j in xrange(N):
        if not NG[j][i]:
            mf.add(j + 1, 100 + i, float("inf"))

cut = mf.max_flow(0, 200)
print "SHIROBAKO" if cut >= W else "BANSAKUTSUKITA"
