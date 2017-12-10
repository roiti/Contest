T = int(raw_input())
for loop in xrange(T):
	f, ba, l, r, t, bo = raw_input().split()
	judge = (l == t == f or l == f == bo or l == bo == ba or l == ba == t or
			 r == t == f or r == f == bo or r == bo == ba or r == ba == t)

	print "YES" if judge else "NO"
