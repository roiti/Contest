S = raw_input()
cnt = 0
a = []
for s in S[::-1]:
    if s == "M":
        a.append(cnt)
    if s == "+":
        cnt += 1
    if s == "-":
        cnt -= 1
a.sort()
print sum(a[len(a) / 2:]) - sum(a[:len(a) / 2])
