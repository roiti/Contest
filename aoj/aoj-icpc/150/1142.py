for i in range(input()):
	train = raw_input()
	ans = set()
	for i in range(len(train)):
		f = train[:i]; rf = f[::-1]
		b = train[i:]; rb = b[::-1]
		ans |= set([f+b,rf+b,f+rb,rf+rb,b+f,rb+f,b+rf,rb+rf])
	print len(ans)

