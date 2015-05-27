from bisect import *
R = 200001
p = [1]*R
p[0] = p[1] = 0
for i in xrange(2,int(R**0.5)):
    if p[i]: p[2*i::i] = [0]*(len(p[2*i::i]))
p = [i for i in xrange(2,R) if p[i]]
    
K = int(raw_input())
N = int(raw_input())
ans = mx = 0
H = []
for i in xrange(bisect(p,K),bisect(p,N)):
    s = str(p[i])
    while len(s) > 1:
        s = str(sum(map(int,list(s))))
    if s in H:
        if   len(H)  > mx: mx,ans = len(H),p[i-len(H)]
        elif len(H) == mx: ans = max(ans, p[i-len(H)])
    while s in H:
        H.pop(0)
    H.append(s)
else:
    if   len(H)  > mx: ans = p[i+1-len(H)]
    elif len(H) == mx: ans = max(ans, p[i+1-len(H)])
print ans
