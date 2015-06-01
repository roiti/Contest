n = int(raw_input())
R = [int(raw_input()) for i in xrange(n)]
mn = R[0]
ans = -1e10
for r in R[1:]:
    ans = max(ans, r - mn)
    mn = min(mn, r)
print ans
