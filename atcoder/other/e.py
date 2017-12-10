def search(i, l, r, rem):
    if abs(P[i] - rem) < 1e-8: return 1
    if memo[l][i - 1] > 0:
        res_l = memo[l][i - 1]
    else:
        res_l = 9999
        for j in xrange(l, i):
            res_l = min(res_l, )
    if memo[i + 1][r] > 0: res_r = memo[i + 1][r]

    res_l = res_r = 9999
    rem_l = sum(P[l:i])
    rem_r = sum(P[i + 1:r + 1])
    s = rem_l + rem_r
    if s < 1e-9: return 1
    for j in xrange(l, i):
        res_l = min(res_l, rem_l / s * search(j, l, i - 1, sum(P[l:i])))
    if res_l == 9999: res_l = 0
    for j in xrange(i + 1, r + 1):
        res_r = min(res_r, rem_r / s * search(j, i + 1, r, sum(P[i + 1:r + 1])))
    if res_r == 9999: res_r = 0
    return 1 + (res_l + res_r) * (1.0 - P[i] / rem)

N = int(raw_input())
P = [float(raw_input()) for i in xrange(N)]

sum_P = [[0] * N for i in xrange(N)]
for i in xrange(N):
    for j in xrange(i, N):
        sum_P[i][j] += P[j] + sum_P[i][j - 1]
memo = [[-1] * N for i in xrange(N)]
ans = 9999
for i in xrange(N):
    ans = min(ans, search(i, 0, N - 1, 1.0))
print %.10f % ans
