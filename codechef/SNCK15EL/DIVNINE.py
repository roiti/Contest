T = int(raw_input())
for loop in xrange(T):
	N = raw_input()
	s = sum(map(int, list(N))) % 9
	if len(N) == 1:
		print min(9 - s, s)
	else:
		t = sum(map(int, list(N[1:])))
		if s == 0:
			print 0
		elif int(N[0]) + t >= 5:
			print min(9 - s, s)
		else:
			print max(9 - s, s)
