def solve(a):
	if type(a[0]) is int:
		return sum(sorted(a)[:len(a)/2+1])/2 + len(a)
	else:
		return sum(sorted(solve(i) for i in a)[:len(a)/2+1])
for i in range(input()):
	A = eval(raw_input().replace("][","],["))
	print solve(A)

