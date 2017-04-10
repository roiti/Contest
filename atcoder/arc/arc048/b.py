N = int(raw_input())
RH = [map(int, raw_input().split()) for i in xrange(N)]

C = [[0]*3 for i in xrange(100005)]
for r, h in RH:
    C[r - 1][h - 1] += 1

D = [0]*100005
for r, _ in RH:
    D[r] += 1
for i in xrange(1, 100005):
    D[i] += D[i - 1]

for r, h in RH:
    w = D[r - 1]
    w += C[r - 1][h%3]
    d = C[r - 1][h - 1] - 1
    l = N - (w + d) - 1
    print w, l, d
