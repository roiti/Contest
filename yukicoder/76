p = [1./12., 1./6., 1./4., 1./12., 1./4., 1./6.]
dp = [0.0]*(1000006)
for i in reversed(xrange(1000000)):
    dp[i] += sum(dp[i+j]*p[j-1] for j in range(1,7))+1.0
dp = dp[::-1][6:]

for loop in xrange(int(raw_input())):
    N = int(raw_input())
    print dp[N-1]