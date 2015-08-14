import itertools as it
b = [map(int, raw_input().split()) for i in xrange(2)]
c = [map(int, raw_input().split()) for i in xrange(3)]

scores = []
for xy in it.combinations([[x, y] for x in range(3) for y in range(3)], 5):
	board = [[0] * 3 for i in xrange(3)]
	for x, y in xy:
		board[y][x] = 1
	s1 = s2 = 0
	for y in xrange(2):
		for x in xrange(3):
			if board[y][x] == board[y + 1][x]:
				s1 += b[y][x]
			else:
				s2 += b[y][x]
	for y in xrange(3):
		for x in xrange(2):
			if board[y][x] == board[y][x + 1]:
				s1 += c[y][x]
			else:
				s2 += c[y][x]

	scores.append([s1, s2])

for i in xrange(125):
	if i % 2 == 0:
		scores.sort(key = lambda x: x[1])
		scores.pop()
	else:
		scores.sort(key = lambda x: x[0])
		scores.pop()

a1, a2 = scores[0]
print a1, a2
