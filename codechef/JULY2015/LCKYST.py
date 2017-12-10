N = int(raw_input())
A = map(int, raw_input().split())

for a in A:
	cnt10 = cnt5 = 0
	while a % 10 == 0:
		a /= 10
		cnt10 += 1
	while a % 5 == 0:
		a /= 5
		cnt5 += 1
	print a * 10 ** cnt10 * 5 ** cnt5 * 4 ** ((cnt5 + 1) / 2)
