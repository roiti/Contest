# coding: utf-8
N,C = map(int,raw_input().split())
a = map(int,raw_input().split())
 
pos = [[-1] for i in xrange(C+1)]
for i in xrange(N):
    pos[a[i]].append(i)
for i in xrange(C+1):
    pos[i].append(N)
 
 
for i in xrange(1,C+1):
    ans = N*(N-1)/2+len(pos[i])-2
    for j in range(1,len(pos[i])):
        tmp = pos[i][j]-pos[i][j-1]-1
        ans -= tmp*(tmp-1)/2
    print ans
