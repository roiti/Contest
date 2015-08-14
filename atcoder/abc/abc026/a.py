A = int(raw_input())
ans = 0
for i in xrange(1, A):
    ans = max(ans, i * (A - i))
print ans
