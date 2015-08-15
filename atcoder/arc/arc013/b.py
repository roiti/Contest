C = int(raw_input())
x = y = z = 0
for i in xrange(C):
    a, b, c = sorted(map(int, raw_input().split()))
    x = max(x, a)
    y = max(y, b)
    z = max(z, c)
print x * y * z
