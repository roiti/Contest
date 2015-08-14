# coding: utf-8
s = raw_input()
for i in xrange(len(s)/2):
    if s[i] == s[-i-1] or "*" in [s[i],s[-i-1]]:
        continue
    print "NO"
    break
else:
    print "YES"
