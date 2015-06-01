while 1:
	e = ans = input()
	if e == 0: break
	for z in range(e):
		z3 = z**3
		if z3 > e: break
		y = int((e-z3)**0.5)
		ans = min(ans,e+y+z-y**2-z3)
	print ans

