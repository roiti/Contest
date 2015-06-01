S = raw_input()
S1, S2 = [], []

ans = pool = 0
for i in xrange(len(S)):
    if S[i] == "/" and len(S1) > 0:
        j = S1.pop()
        ans += i - j
        a = i - j
        while (len(S2) > 0 and S2[-1][0] > j):
            a += S2.pop()[1]
        S2.append([j, a])
    if S[i] == "\\":
        S1.append(i)
print ans
if len(S2) > 0:
    print len(S2), " ".join(map(str, [a for j, a in S2]))
else:
    print 0
