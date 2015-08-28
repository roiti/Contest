T, A, B = map(int, raw_input().split())

ans = [""] * T
if A > T or B > T:
	print "NO"
else:
	for i in xrange(T):
		if (A == 0 and i != T - 1) or A < 0:
			ans[i] += "v"
			A += 1
		elif A > 0:
			ans[i] += "^"
			A -= 1
	for i in xrange(T - 1, -1, -1):
		if (B == 0 and i != 0) or B < 0:
			ans[i] += "<"
			B += 1
		elif B > 0:
			ans[i] += ">"
			B -= 1

	if "" not in ans:
		print "YES"
		for a in ans:
			print a
	else:
		print "NO"
