dic = {"i":1,"x":10,"c":100,"m":1000}
for r in range(input()):
	a,b = raw_input().split()
	s = 0
	for i in range(len(a)-1,-1,-1):
		if a[i] in "ixcm":
			try: s += int(a[i-1])*dic[a[i]]
			except: s += dic[a[i]]
	for i in range(len(b)-1,-1,-1):
		if b[i] in "ixcm":
			try: s += int(b[i-1])*dic[b[i]]
			except: s+= dic[b[i]]
	s = str(s)
	ans = ""
	for i in range(len(s)):
		if int(s[-i-1]) > 0:
			ans += "ixcm"[i] + s[-i-1]
	print ans[::-1].replace("1","")

