N = int(raw_input()) + 1
ans = 0
for i in xrange(10):
    ans += N / 10**(i + 1) * 10**i + min(10**i, max(0, N % 10**(i + 1) - 10**i))
print ans
