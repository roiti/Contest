N = int(raw_input())
used = []
for i in xrange(N):
    w = raw_input()
    if w in used or (i > 0 and w[0] != used[-1][-1]):
        print "WIN" if i % 2 else "LOSE"
        break
    used.append(w)
else:
    print "DRAW"
