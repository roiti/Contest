import heapq
N = int(raw_input())
_A = [i*100000 for i in map(int,raw_input().split())]
B = map(int,raw_input().split())

ans = 1500
for sp in xrange(N):
    A = _A[:]
    heapq.heapify(A)
    for i in xrange(sp, N+sp):
        i %= N
        a = heapq.heappop(A)
        a += B[i]/2*100000+1
        heapq.heappush(A,a)
    ans = min(ans, max([heapq.heappop(A)%100000 for i in xrange(N)]))
print ans
