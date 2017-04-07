S = raw_input()
T = S[0]
for s in S[1:]:
    if T[-1] == s: continue
    T += s
print len(T) - 1
