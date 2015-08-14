from collections import defaultdict
mod = 10**9+7
 
def calc(n):
    res = 0
    i = 2
    while i*i <= n:
        while n%i == 0:
            n /= i
            count[i] += 1
        i += 1
    if n > 1: count[n] += 1
 
A,B = map(int,raw_input().split())
count = defaultdict(int)
for i in xrange(B+1,A+1): calc(i)
ans = 1
for i in count.values():
    ans = (ans*(i+1))%mod
print ans
