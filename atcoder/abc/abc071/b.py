S = raw_input()
for c in [chr(ord("a") + i) for i in xrange(26)]:
    if c in S:
        continue
    else:
        print c
        break
else:
    print "None"
