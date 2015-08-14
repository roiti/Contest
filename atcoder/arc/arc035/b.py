from collections import defaultdict
mod = 10**9+7
def fact(n):
    res = 1
    while n:
        res = res*n%mod
        n -= 1
    return res
    
N = int(raw_input())
T = sorted([int(raw_input()) for i in xrange(N)])
hist = defaultdict(int)
for t in T:
    hist[t] += 1
 
time = 0
pena = 0
for t in T:
    time += t
    pena += time
comb = 1
for i in hist.values():
    comb = comb*fact(i)%mod;
print pena
print comb
