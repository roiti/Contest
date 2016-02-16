S = list(raw_input())
while S:
    j = 0
    rem = []
    print S
    for i in xrange(len(S)):
        if S[i] == "titech"[j]:
            if j >= 1:
                if not S[:i].count("t") > 1: continue
            if j >= 2:
                if not S[:i].count("i") > 1: continue
            if j >= 3:
                if not S[:i].count("t") > 2: continue
            if j >= 4:
                if not S[:i].count("e") > 1: continue
            if j >= 5:
                if not S[:i].count("c") > 1: continue
            j += 1
            rem.append(i)
        if j == 6:
            for k in reversed(rem):
                del S[k]
            break
    else:
        print "No"
        break
else:
    print "Yes"
