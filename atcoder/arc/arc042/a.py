N, M = map(int, raw_input().split())
R = [(N - i - 1) for i in xrange(N)]
for i in xrange(M):
    a = int(raw_input()) - 1
    R[a] = N + i
R = sorted([[v, i + 1] for i, v in enumerate(R)], reverse = True)
for r in R:
    print r[1]
