mod = 10 ** 9 + 7
 
def calc(n, m):
    res = 1
    for i in xrange(m):
        res *= (n - i)
    for i in xrange(1, m + 1):
        res /= i
    return res % mod
 
N, K = map(int, raw_input().split())
if N <= K:
    print calc(N, K % N)
else:
    print calc(N + K - 1, N - 1)
