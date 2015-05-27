n = int(raw_input())
a = map(int, raw_input().split())
hist = [0] * 10000
for i in a:
    hist[i] += 1

ans = 0
for i in xrange(10000):
    if hist[i] > 1:
        hist[i + 1] += hist[i] - 1
        ans += hist[i] - 1
        hist[i] = 1
print ans
