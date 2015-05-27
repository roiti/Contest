N = int(raw_input())
ab = [map(int, raw_input().split()) for i in xrange(N)]

l, r = 1, 10**10
x = (l+r)/2
ax, mn = 0, 10**50
for loop in xrange(40):
    abx = [a+b*x for a,b in ab]
    tmp = max(abx) - min(abx)
    if tmp < mn:
        mn = tmp
        ax = x
    if tmp == mn:
        ax = min(x, ax)
    abx1 = [a+b*(x+1) for a,b in ab]
    tmp1 = max(abx1) - min(abx1)
    if tmp1 < tmp:
        l = x
    else:
        r = x
    x = (l+r)/2 if r-l > 0 else x+1
print ax