def f(n):
    res = 0
    for s in str(n):
        res += int(s)
    return res
    
N = int(raw_input())
ans = []
for n in xrange(max(0,N-1000),N+1000):
    if n+f(n) == N:
        ans.append(n)
print len(ans)
for a in ans: print ana,nb = map(int,raw_input().split())
a = set(map(int,raw_input().split()))
b = set(map(int,raw_input().split()))
print len(a&b)*1.0/len(a|b)
