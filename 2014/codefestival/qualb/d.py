N = int(raw_input())
h = [int(raw_input()) for i in range(N)]
l = [0]*N
r = [0]*N
for i in range(1,N):
    if h[i] >= h[i-1]:
        l[i] = l[i-1]+1
for i in range(N-2,-1,-1):
    if h[i] >= h[i+1]:
        r[i] = r[i+1]+1
 
for i in range(N):
    p = i
    while p < N and h[p] <= h[i]:
        p += r[p]+1
    R = p-i
    p = i
    while p > -1 and h[p] <= h[i]:
        p -= l[p]+1
    L = i-p
    print R+L-2
