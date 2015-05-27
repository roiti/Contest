import heapq
N = int(raw_input())
S = [raw_input() + "{" for i in xrange(N)]
M = sum(map(len, S)) - N
heapq.heapify(S)
T = ""

for i in xrange(M):
    s = heapq.heappop(S)
    if s == "": continue
    T += s[0]
    heapq.heappush(S, s[1:])
print T
