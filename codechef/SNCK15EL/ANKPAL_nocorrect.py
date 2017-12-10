s = raw_input()
Q = int(raw_input())
for loop in xrange(Q):
	i, j, k, l = map(int, raw_input().split())
	i -= 1; k -= 1
	ss = s[:i] + s[i:j][::-1] + s[j:]
	print "YES" if ss[k:l] == ss[k:l][::-1] else "NO"
