while 1:
	a = raw_input()
	if a == ".": break
	a = "".join([i for i in a if i in "()[]"])
	while len(a) > 0:
		if   "()" in a: a = a.replace("()","")
		elif "[]" in a: a = a.replace("[]","")
		else: break
	print "yes" if len(a) == 0 else "no"


