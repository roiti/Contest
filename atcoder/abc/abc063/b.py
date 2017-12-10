S = sorted(list(raw_input()))
for i in xrange(len(S) - 1):
    if S[i] == S[i + 1]:
        print "no"
        exit()
print "yes"
