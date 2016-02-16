import itertools as it
S = raw_input()
if len(set(list(S))) > 5:
    print -1
    exit() 

A = list(set(list(S)))
for comb in it.permutations("13579"):
    conv = zip(A, comb)
    s = S
    for i, j in conv:
        s = s.replace(i, j)
    s = int(s)
    if s == 1: continue
    i = 2
    while i * i <= s:
        if s % i == 0:
            break
        i += 1
    else:
        print s
        break
else:
    print -1
