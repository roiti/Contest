n = int(raw_input())
ls = []
bp = 0
for i in range(n):
	cmd = raw_input()
	if cmd[0] == "i":
		ls.append(cmd[7:])
	elif cmd[6] == " ":
		try:
			x = ls[::-1].index(cmd[7:])
			if x!=-1:
				del ls[-x-1]
		except:
			pass
	elif cmd[6] == "F":
		ls.pop()
	else:
		bp += 1

print " ".join(map(str, ls[bp:][::-1]))

