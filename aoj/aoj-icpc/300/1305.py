while 1:
	n = input()
	if n == 0: break
	ans = {}
	for i in range(n):
		group,name = raw_input().split(":")
		if i == 0: first = group
		ans[group] = set(name[:-1].split(","))
	while 1:
		for key in ans:
			flag = 0
			if key == first: continue
			for key1 in ans:
				if key in ans[key1]:
					ans[key1] |= ans[key]
					ans[key1].discard(key)
					flag = 1
			if flag:
				del ans[key]
				break
		if flag == 0: break
	print len(ans[first])

