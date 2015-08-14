import heapq
dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])
H, W = map(int, raw_input().split())
S = map(int, raw_input().split())
S = (S[0]-1, S[1]-1)
G = map(int, raw_input().split())
P = [map(int, raw_input().split()) for i in xrange(H)]
 
ans = sum(map(sum, P))
visited = set([])
heap = []
heapq.heappush(heap, (0, S))
while len(visited) < H*W:
    cost, pos = heapq.heappop(heap)
    if pos in visited: continue
    visited.add(pos)
    ans += -cost
    x,y = pos
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if 0 <= nx < W and 0 <= ny < H:
            npos = (nx, ny)
            if npos in visited: continue
            ncost = -(P[ny][nx]*P[y][x])
            heapq.heappush(heap, (ncost, npos))
print ans
