dxy = zip([0, 1, 0, -1, 0], [0, 0, 1, 0, -1])
a = [map(int, raw_input().split()) for i in xrange(4)]
b = [[j % 16 for j in xrange(4 * i + 1, 4 * i + 5)] for i in xrange(4)]

for y in xrange(4):
	for x in xrange(4):
		for dx, dy in dxy:
			nx, ny = x + dx, y + dy
			if not (0 <= nx < 4 and 0 <= ny < 4): continue
			if a[ny][nx] == b[y][x]:
				break
		else:
			print "No"
			exit()
print "Yes"
