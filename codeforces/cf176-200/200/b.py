a = raw_input()
b = []
size = 0
for c in a:
	b.append(c)
	size += 1
	while size >= 2:
		if b[-2:] in [["+","+"], ["-","-"]]:
			b.pop(); b.pop()
			size -= 2
		else:
			break
print "Yes" if size == 0 else "No"
