S = raw_input()
ans = -999999
for i in xrange(len(S)):
    s = S[i:] + S[:i]
    for j in xrange(10):
        for k in map(str, range(10)):
            s = s.replace("+0" + k, "+" + k)
            s = s.replace("-0" + k, "-" + k)
    if s[0] in "+-" or s[-1] in "+-": continue
    ans = max(ans, eval(s))
print ans