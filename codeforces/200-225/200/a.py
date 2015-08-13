a, b = map(int, raw_input().split())

cnt = 0
while 1:
	if b == 1:
		cnt += a
		break
	elif a == b:
		cnt += 1
		break
	elif a > b:
		cnt += (a - 1) / b
		a -= (a - 1) / b * b
	else:
		cnt += (b - 1) / a
		b -= (b - 1) / a * a

print cnt
