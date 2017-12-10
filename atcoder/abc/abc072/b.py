s = raw_input()
print "".join(s[i] for i in xrange(len(s)) if i%2 == 0)

