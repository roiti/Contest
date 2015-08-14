S = raw_input()
N = int(raw_input())
a = set([])
for s1 in S:
	for s2 in S:
		a.add(s1 + s2)

a = sorted(list(a))
print a[N - 1]
