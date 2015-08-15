import heapq
N, K = map(int, raw_input().split())
X = zip(map(int, raw_input().split()), range(N))

a = []
b = sorted(X[:K])
for i, j in b[:-1]:
    heapq.heappush(a, (-i, j))

old, rank = b[-1]
print rank + 1
for i in xrange(K, N):
    if X[i][0] < old:
        heapq.heappush(a,(-X[i][0], X[i][1]))
        old, rank = heapq.heappop(a)
        old *= -1
    print rank + 1
