N, S, T = map(int,raw_input().split())
A = [input() for i in xrange(N)]
W = 0
ans = 0
for a in A:
    W += a
    if S <= W <= T:
        ans += 1
print ans
