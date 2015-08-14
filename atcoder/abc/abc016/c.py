# coding: utf-8
n,m = map(int,raw_input().split())
friend = [[] for _ in range(n)]
pop = [0]*n
for roop in range(m):
    a,b = map(int,raw_input().split())
    a -= 1; b -= 1
    friend[a].append(b)
    friend[b].append(a)
for i in range(n):
    ff = set([])
    if len(friend[i]) == 0:
        print 0
        continue
    for j in friend[i]:
        ff |= set(friend[j])
    print len(ff-set(friend[i]))-1
    
