S = raw_input()
ans = [0] * 6
for i, c in enumerate("ABCDEF"):
    ans[i] = S.count(c)
print " ".join(map(str, ans))
