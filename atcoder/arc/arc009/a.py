N = int(raw_input())
ans = 0
for loop in xrange(N):
    a, b = map(int, raw_input().split())
    ans += a * b
print int(ans * 1.05)
