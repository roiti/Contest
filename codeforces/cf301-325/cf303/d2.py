n = int(raw_input())
que = sorted(map(int, raw_input().split()))
ans = 0
s = 0
for i in xrange(n):
    if que[i] >= s:
        ans += 1
        s += que[i]
print ans
