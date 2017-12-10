from collections import defaultdict 

N = int(raw_input())
d = defaultdict(int)
for i in xrange(N):
    A = int(raw_input())
    d[A] = (d[A] + 1) % 2
ans = 0
for v in d.values():
    ans += v
print ans
