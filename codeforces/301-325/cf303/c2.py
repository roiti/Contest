inf = 10 ** 15
n = int(raw_input())
xh = [map(int, raw_input().split()) for i in xrange(n)] + [[inf, 0]]
ans = 0
pos = -inf
for i in xrange(n):
    x, h = xh[i]
    if x - h > pos:
        pos = x
        ans += 1
    elif x + h < xh[i + 1][0]:
        pos = x + h
        ans += 1
    else:
        pos = x
print ans
