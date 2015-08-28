able = set([(0, 0)])
for loop in xrange(3):
	nable = able.copy()
	for (x, y) in able:
		for (nx, ny) in (x-2,y-1),(x-2,y+1),(x-1,y-2),(x-1,y+2),(x+1,y-2),(x+1,y+2),(x+2,y-1),(x+2,y+1):
			nable.add((nx, ny))
	able = nable

X, Y = map(int, raw_input().split())
print "YES" if (X, Y) in able else "NO"
