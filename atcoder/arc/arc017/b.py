N, K = map(int, raw_input().split())
A = [int(raw_input()) for i in xrange(N)]
D = [A[i + 1] - A[i] for i in xrange(N - 1)]

cnt = 0
for i in xrange(K - 1):
    if D[i] <= 0: cnt += 1

ans = 1 if cnt == 0 else 0
for i in xrange(K - 1, N - 1):
    if D[i - K + 1] <= 0: cnt -= 1
    if D[i] <= 0: cnt += 1
    if cnt == 0: ans += 1
print ans
