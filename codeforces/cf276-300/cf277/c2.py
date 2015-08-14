n,p = map(int,raw_input().split())
p = n-p if p > n/2 else p-1
s = list(raw_input())
al = map(ord,s)
updown,l,r = 0,n/2,-1
for i in xrange(n/2):
    d = abs(al[i]-al[-i-1])
    updown += min(d,26-d)
    if d:
        l = min(l,i)
        r = max(r,i)
print updown+r-l+min(abs(r-p),abs(l-p)) if updown else 0
