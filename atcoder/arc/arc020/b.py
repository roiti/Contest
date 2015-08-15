n, c = map(int, raw_input().split())
a = [int(raw_input()) for i in xrange(n)]
ans = 1e10
for i in xrange(1, 11):
    for j in xrange(1, 11):
        if i == j: continue
        tmp = 0
        for k in xrange(n):
            if k % 2 == 0 and a[k] != i:
                tmp += c
            if k % 2 == 1 and a[k] != j:
                tmp += c
        ans = min(ans, tmp)
print ans
