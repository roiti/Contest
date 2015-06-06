from itertools import repeat
n = int(raw_input())
a = map(int, raw_input().split())
a = sorted([(i + x, i, x) for i, x in enumerate(a)])

for i in xrange(n - 1):
	if a[i][0] == a[i + 1][0]:
		print ":("
		exit()

ans = []
for i, z in enumerate(a):
	s, j, x = z
	ans.append(x + j - i)
print " ".join(map(str, ans))
