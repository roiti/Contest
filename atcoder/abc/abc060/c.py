N, T = map(int, raw_input().split())    
t = map(int, raw_input().split())   
ans = 0
cur = 0
for i in xrange(N - 1):
    if t[i + 1] - t[i] > T:
        ans += t[i] + T - cur
        cur = t[i + 1]
ans += t[N - 1] + T - cur
print ans

