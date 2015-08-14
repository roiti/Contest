N, M = map(int, raw_input().split())

d = range(1, N + 1)
now = 0
for loop in xrange(M):
    nxt = int(raw_input())
    if nxt == now: continue
    pos = d.index(nxt)
    now, d[pos] = nxt, now

for i in d:
    print i
