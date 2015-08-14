import heapq
N = int(raw_input())
tree = [[] for i in xrange(N)]
for loop in xrange(N-1):
    a,b = map(int,raw_input().split())
    a -= 1; b -= 1
    tree[a].append(b)
    tree[b].append(a)
    
cand = tree[0][:]
heapq.heapify(cand)
used = [False]*N
used[0] = True
ans = [1]
for loop in xrange(N-1):
    nxt = heapq.heappop(cand)
    ans.append(nxt+1)
    used[nxt] = True
    for i in tree[nxt]:
        if not used[i]:
            heapq.heappush(cand,i)
print " ".join(map(str,ans))
