s = raw_input()
for i in xrange(0, 10):
	if str(i) + "+" in s:
		s = s.replace(str(i) + "+", str(i) + "-")
		break
	if str(i) + "-" in s:
		s = s.replace(str(i) + "-", str(i) + "+")
		break
print eval(s)
