eps = 1e-9
n = int(raw_input())

a = 1 + 8 * n
if a == int(a ** 0.5 + eps) ** 2:
	if int(-1 + a ** 0.5 + eps) % 2 != 0:
		print -1
	else:
		print int((-1 + a**0.5 + eps) / 2)
else:
	print -1
