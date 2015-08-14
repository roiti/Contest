mod = 10**9+7
A = int(raw_input())
B = int(raw_input())
ans = 0
for i in xrange(A,B+1):
    ans = (ans + i*i*(i+1)/2)%mod
print ans
