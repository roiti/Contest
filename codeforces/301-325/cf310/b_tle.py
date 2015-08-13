import bisect
n, m = map(int, raw_input().split())
lr = [map(int, raw_input().split()) for i in xrange(n)]
b = [[lr[i + 1][0] - lr[i][1], lr[i + 1][1] - lr[i][0], i] for i in xrange(n - 1)]
bmx = max(br for bl, br, i in b)
bmn = min(bl for bl, br, i in b)
b.sort(key = lambda x: x[1])
a = zip(map(int, raw_input().split()), range(1, m + 1))
a = [[aa, i] for aa, i in a if bmn <= aa <= bmx]
ai = sorted(a)
a = [aa for aa, i in sorted(a)]
ans = []

if len(a) == 0:
	print "No"
	exit()

for bl, br, i in b:
	idx = bisect.bisect_left(a, bl)
	if bl <= a[idx] <= br:
		ans.append([i, ai.pop(idx)[1]])
		a.pop(idx)
	if len(a) == 0:
		break

ans = [j for i, j in sorted(ans)]
if len(ans) == n - 1:
	print "Yes"
	print " ".join(map(str, ans))
else:
	print "No"

