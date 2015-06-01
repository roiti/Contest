while 1:
	a,L = raw_input().split()
	if a == L == "0": break
	a = a.zfill(int(L))
	his = [0]*21
	his[0] = a
	i = 0
	while 1:
		i += 1
		a = str(int("".join(sorted(a)[::-1])) - int("".join(sorted(a)))).zfill(int(L))
		if a in his: break
		his[i] = a
	print his.index(a),int(a),i-his.index(a)

