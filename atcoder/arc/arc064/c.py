N, x = map(int, raw_input().split())
a = map(int, raw_input().split())
ans = 0
if a[0] > x:
    ans += a[0] - x
    a[0] = x
if a[-1] > x:
    ans += a[-1] - x
    a[-1] = x
for i in xrange(N - 1):
    if a[i] + a[i + 1] > x:
        ans += a[i + 1] - (x - a[i])
        a[i + 1] = x - a[i]
print ans
