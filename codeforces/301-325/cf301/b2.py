n, k, p, x, y = map(int, raw_input().split())
a = map(int, raw_input().split())
cnt = 0
for i in xrange(k):
    if a[i] >= y: cnt += 1

m = (n + 1) / 2
ans = []
while len(ans) < n - k:
    if cnt < m:
        ans.append(y)
    else:
        ans.append(1)
    cnt += 1
    
if sum(a) + sum(ans) <= x and cnt >= m:
    print " ".join(map(str, ans))
else:
    print -1
