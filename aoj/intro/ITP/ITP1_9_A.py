w = raw_input().lower()
sum = 0
while True:
    t = raw_input().split()
    if t[0] == "END_OF_TEXT":
        break
    else:
        for ti in t:
            if ti.lower() == w:
                sum += 1
print sum

