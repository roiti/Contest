N = int(raw_input())
K = int(raw_input())
x = map(int, raw_input().split())   
ans = 0
for i in xrange(N):
    ans += 2*min(x[i], abs(K - x[i]))
print ans

