N = int(raw_input())
exp = 3000000
GD = [map(int, raw_input().split()) + [i] for i in xrange(N)]

G = sorted([[g - exp / 100 * d, i] for g, d, i in GD], reverse = True)
if 6 * max(G)[0] >= exp:
	print "YES"
	for i in xrange(6):
		print max(G)[1] + 1
else:
	print "NO"


