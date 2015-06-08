T = int(raw_input())
for loop in xrange(T):
	n, sx, sy, ex, ey, bx, by = map(int, raw_input().split())
	d = abs(sx - ex) + abs(sy - ey)
	if sy == ey == by:
		if sx < bx < ex or ex < bx < sx:
			print d + 2
		else:
			print d
	elif sx == ex == bx:
		if sy < by < ey or ey < by < sy:
			print d + 2
		else:
			print d
	else:
		print d
