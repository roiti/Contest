s = raw_input()
t = raw_input()
if len(s) != len(t):
    print -1
else:    
    for i in xrange(len(s)+1):
        if s == t:
            print i
            break
        s = s[-1]+s[:-1]
    else:
        print -1
