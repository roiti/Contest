S, D = "Stannis", "Daenerys"
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a = [ai % 2 for ai in a]
o, e = a.count(1), a.count(0)
if n == k:
	print S if o % 2 == 1 else D
	exit()

for i in xrange(n - k - 1):
	if i % 2 == 0:
		if e > 0:
			e -= 1
		else:
			o -= 1
	else:
		if o > 0:
			o -= 1
		else:
			e -= 1

if (n - k) % 2 == 1:
	if o > o % 2 == 0 or e == 0:
		o -= 1
	else:
		e -= 1
else:
	if o % 2 == 1 or e == 0:
		o -= 1
	else:
		e -= 1
print S if o % 2 == 1 else D
