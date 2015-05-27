def gcd(a,b):
    while b: a,b = b,a%b
    return a
    
M,N = map(int,raw_input().split())
d = gcd(M,N)
M,N = M/d,N/d

ans = 0
while 0 < M != N:
    if M > N:
        ans += M/N
        M -= M/N*N
    else:
        M,N = N,M
        ans += 1
print max(0,ans-1)