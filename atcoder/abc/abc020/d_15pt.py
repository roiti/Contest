mod = 10**9+7
def gcd(a,b):
    while b: a,b = b,a%b
    return a
 
def lcm(a,b):
    return a*b/gcd(a,b)
 
N,K = map(int,raw_input().split())
ans = 0
 
for i in xrange(1,N+1):
    ans = (ans+lcm(i,K))%mod
print ans
