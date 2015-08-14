dxy = zip([1, 0, -1, 0], [0, 1, 0, -1])
N, M = map(int, raw_input().split())
b = [map(int, list(raw_input())) for i in xrange(N)]

a = [[0] * M for i in xrange(N)]

k = 1
for d in xrange(N / 2 + 1):
	for y in [d, N - 1 - d]:
		for x in xrange(1, M - 1):
			if b[y][x] != 0:
				a[y + k][x] += b[y][x]
				tmp = b[y][x]
				for dx, dy in dxy:
					b[y + k + dy][x + dx] -= tmp
		k *= -1

for x in [0, M - 1]:
	for y in xrange(1, N - 1):
		if b[y][x] != 0:
			a[y][x + k] += b[y][x]

for line in a:
	print "".join(map(str, line))
