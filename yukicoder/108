def dp(n1,n2,n3):
    if memo[n1][n2][n3] > -1: return memo[n1][n2][n3]
    
    n123 = n1+n2+n3
    memo[n1][n2][n3] = N*1.0/n123
    if n1 > 0: memo[n1][n2][n3] += dp(n1-1,n2  ,n3  )*n1/n123
    if n2 > 0: memo[n1][n2][n3] += dp(n1+1,n2-1,n3  )*n2/n123
    if n3 > 0: memo[n1][n2][n3] += dp(n1  ,n2+1,n3-1)*n3/n123
    return memo[n1][n2][n3]
    
N = int(raw_input())
A = map(int,raw_input().split())
memo = [[[-1]*101 for i in xrange(101)] for j in xrange(101)]
memo[0][0][0] = 0.0
need = [0]*3
for a in A:
    if a == 0: need[2] += 1
    if a == 1: need[1] += 1
    if a == 2: need[0] += 1
print dp(*need)