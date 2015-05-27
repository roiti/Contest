s1 = raw_input()
N = min(2, int(raw_input()))
s2 = raw_input()
S = set([s1])
while N:
    nS = set([])
    for s in S:
        nS.add(s[0] + s[2] + s[1])
        nS.add(s[1] + s[0] + s[2])
    S = nS.copy()
    N -= 1
print "FAILURE" if s2 in S else "SUCCESS"