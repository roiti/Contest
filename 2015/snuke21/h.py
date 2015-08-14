a, b, c = map(int, raw_input().split())

d = c - a
if d <= 0:
	print "NO"
else:
	if b <= d:
		print "YES"
	else:
		print "NO"
