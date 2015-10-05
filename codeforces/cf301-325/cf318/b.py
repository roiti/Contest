n = int(raw_input())
h = map(int, raw_input().split())

h[0] = h[-1] = 1
for i in xrange(1, n):
    h[i] = min(h[i], h[i - 1] + 1, i + 1)
for i in xrange(n - 2, -1, -1):
    h[i] = min(h[i], h[i + 1] + 1, i + 1)
print max(h)
