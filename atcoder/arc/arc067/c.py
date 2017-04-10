mod = 10**9 + 7

def factrize(n):
    res = [0]*1001
    i = 2
    while i*i <= n:
        while n%i == 0:
             n /= i
             res[i] += 1
	i += 1
    if n > 1: res[n] += 1
    return res

N = int(raw_input())

ans = 1
cnt = [0]*1001
for i in xrange(1, N + 1):
    tmp = factrize(i)
    for j in xrange(2, 1001):
        cnt[j] += tmp[j]

for i in xrange(2, N + 1):
    ans = ans * (cnt[i] + 1) % mod 
print ans
