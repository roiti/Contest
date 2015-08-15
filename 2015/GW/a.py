import itertools as it
prob = [25,39,51,76,163,111,128,133,138]
ans = [0, 58, 136]
for i in xrange(1, len(prob) + 1):
    for score in it.combinations(prob, i):
        s = sum(score)
        ans.append(s)
        ans.append(s + 58)
        ans.append(s + 136)
for a in sorted(list(set(ans))):
    print a
