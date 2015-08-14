N = int(raw_input())
s = map(int, list(raw_input()))
g = map(int, list(raw_input()))

ans = 0
for i in xrange(N):
    ans += min(abs(s[i] - g[i]), 10 - abs(s[i] - g[i]))
    
print ans
