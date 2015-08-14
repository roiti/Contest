import bisect
N = int(raw_input())
H = map(int,raw_input().split())
 
r = [0]*N
H = H[::-1]
for i in range(1, N):
    j = 0
    while H[i-j-1] < H[i]:
        j += 1
        j += r[i-j]
        if j == i:
            break
    r[i] = j
r = r[::-1]
 
A = [0]*(N+1)
for i in xrange(N-1):
    A[i+1] += 1
    A[min(i+r[i]+2,N)] -= 1
for i in xrange(1,N):
    A[i] += A[i-1]
for i in xrange(N):
    print A[i]
