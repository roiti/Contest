dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])

H, W = map(int, raw_input().split())
C = [list(raw_input()) for i in xrange(H)]

for y in xrange(H):
	for x in xrange(W):
		if C[y][x] == "s":
			sx, sy = x, y
			C[y][x] = "."
		if C[y][x] == "g":
			gx, gy = x, y
			C[y][x] = "."

que = [[sx, sy]]
while que:
	x, y = que.pop()
	if (x, y) == (gx, gy):
		print "Yes"
		break
	for dx, dy in dxy:
		nx, ny = x + dx, y + dy
		if 0 <= nx < W and 0 <= ny < H:
			if C[ny][nx] == "#" or C[ny][nx] == "X": continue
			que.append([nx, ny])
			C[ny][nx] = "X"
else:
	print "No"

