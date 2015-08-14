N, A, B = map(int, raw_input().split())
pos = 0
for loop in xrange(N):
	s, d = raw_input().split()
	d = int(d)
	if s == "East":
		pos += min(max(A, d), B)
	else:
		pos -= min(max(A, d), B)

if pos == 0:
	print pos
elif pos > 0:
	print "East", pos
else:
	print "West", -pos
