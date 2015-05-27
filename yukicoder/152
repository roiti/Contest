def gcd(a,b):
    while b: a,b = b,a%b
    return a
    
N = int(raw_input())
ans = 0
for m in xrange(1,int((N/8)**0.5)+1):
    for n in xrange(1,m):
        if (m-n)%2 != 1: continue
        if 4*((m*m+n*n) + (2*m*n) + (m*m-n*n)) > N: break
        if gcd(m,n) == 1: ans += 1
print ans%1000003