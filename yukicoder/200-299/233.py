import itertools as it

C = set([])
a = "iaaeuu"
b = "nbmgr"
boin = set(["".join(c) for c in it.permutations(a, 6)])
shin = set(["".join(c) for c in it.permutations(b, 5)])
for bo in boin:
	for si in shin:
		s = ""
		for i in xrange(5):
			s += si[i] + bo[i]
		for k in xrange(11):
			C.add(s[:k] + bo[5] + s[k:])

N = int(raw_input())
S = set([raw_input() for i in xrange(N)])

ans = C - S
if len(ans) == 0:
	print "NO"
else:
	print list(ans)[0]

