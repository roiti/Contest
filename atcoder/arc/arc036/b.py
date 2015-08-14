N = int(raw_input())
h = [int(raw_input()) for i in xrange(N)]
 
l = [0]*N
r= [0]*N
seq = 0
for i in xrange(N-1):
    if h[i+1] > h[i]:
        seq += 1
        l[i+1] += seq
    else:
        seq = 0
seq = 0
for i in xrange(N-1,0,-1):
    if h[i] < h[i-1]:
        seq += 1
        r[i-1] += seq
    else:
        seq = 0
 
ans = max(map(sum,zip(l,r)))
print ans+1
