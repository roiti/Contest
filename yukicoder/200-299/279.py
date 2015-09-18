s = raw_input()
t = r = e = 0
for c in s:
    if c == "t": t += 1
    if c == "r": r += 1
    if c == "e": e += 1
print min(t, r, e / 2)
