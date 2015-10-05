import heapq
n = int(raw_input())
p = map(int, raw_input().split())
q = map(int, raw_input().split())
q = [q[i] / 100. for i in xrange(n)]

que = [(-p[i] * q[i] / 1000.0, i) for i in xrange(n)]
heapq.heapify(que)
_ans, ans = -1.0, 0.0
i = 1
while ans - _ans > 5e-6:
    _ans = ans
    pq, j = heapq.heappop(que)
    ans += -i * pq
    heapq.heappush(que, (pq * (1.0 - q[j]), j))
    i += 1
print "%.10f" % ans
