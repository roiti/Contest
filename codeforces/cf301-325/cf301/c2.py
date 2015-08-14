drc = zip([0, 1, 0, -1], [1, 0, -1, 0])
n, m = map(int, raw_input().split())
C = [list(raw_input()) for i in xrange(n)]
r1, c1 = map(int, raw_input().split())
r1 -= 1; c1 -= 1
r2, c2 = map(int, raw_input().split())
r2 -= 1; c2 -= 1

que = [[r1, c1]]
visited = [[False] * m for i in xrange(n)]
while que:
    r, c = que.pop()
    if (r, c) == (r2, c2):
        break
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and ((nr, nc) == (r2, c2) or C[nr][nc] == "."):
            if visited[nr][nc]: continue
            visited[nr][nc] = True
            que.append([nr, nc])
else:
    print "NO"
    exit()

cnt = 0
for dr, dc in drc:
    nr, nc = r2 + dr, c2 + dc
    if 0 <= nr < n and 0 <= nc < m and C[nr][nc] == ".":
       cnt += 1

dist = abs(r1 - r2) + abs(c1 - c2)
if dist == 0 and cnt >= 1:
    print "YES"
elif dist == 1 and (C[r2][c2] == "X" or cnt >= 1):
    print "YES"
elif dist > 1 and (C[r2][c2] == "X" or cnt >= 2):
    print "YES"
else:
    print "NO"
