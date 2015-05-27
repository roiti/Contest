from collections import defaultdict

def hist():
    return [0]*26
    
alpha = "abcdefghijklmnopqrstuvwxyz"
atoi = {alpha[i]:i for i in xrange(26)}
pos = [[] for i in xrange(26)]

x = map(int,raw_input().split())
s = [atoi[si] for si in raw_input()]
n = len(s)

sums = defaultdict(hist)
sum = 0
ans = 0
for i in xrange(n):
    sum += x[s[i]]
    ans += sums[sum-x[s[i]]][s[i]]
    sums[sum][s[i]] += 1
print ans
