s = raw_input()
n = len(s)
if s[0] == s[-1]:
    print "First" if n%2 == 0 else "Second"
else:
    print "Second" if n%2 == 0 else "First"
