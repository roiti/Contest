import heapq
dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])
ref = {"U":(0, -1), "D":(0, 1), "R":(1, 0), "L":(-1, 0)}
W, H, N = map(int, raw_input().split())
sx, sy, gx, gy = map(int, raw_input().split())
cost = [[0] * (W + 1) for i in xrange(H + 1)]
for loop in xrange(N):
    x, y = map(int, raw_input().split())
    T, step = raw_input().split()
    for i in xrange(int(T)):
        for s in step:
            dx, dy = ref[s]
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:
                x, y = nx, ny
                cost[y][x] += 1


G = [[1e15] * (W + 1) for i in xrange(H + 1)]
que = [[0, sx, sy]]
while que:
    c, x, y = heapq.heappop(que)
    if (x, y) == (gx, gy): break
    if c > G[y][x]: continue
    for dx, dy in dxy:
       nx, ny = x + dx, y + dy
       if 0 <= nx <= W and 0 <= ny <= H:
           nc = c + cost[ny][nx]
           if G[ny][nx] > nc:
               heapq.heappush(que, [nc, nx, ny])
               G[ny][nx] = nc

print G[gy][gx]
