N = int(raw_input())
R = B = 0
for i in xrange(N):
	row = raw_input()
	R += row.count("R")
	B += row.count("B")
print "TAKAHASHI" if R > B else "AOKI" if B > R else "DRAW"
