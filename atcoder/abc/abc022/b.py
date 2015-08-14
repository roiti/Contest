from collections import defaultdict
N = int(raw_input())
hist = defaultdict(int)
for loop in xrange(N):
    a = int(raw_input())
    hist[a] += 1
ans = 0
for v in hist.values():
    ans += v - 1
print ans
