n = int(raw_input())
k1 = map(int, raw_input().split()[1:])
k2 = map(int, raw_input().split()[1:])
for turn in xrange(1, 1000000):
    a, b = k1.pop(0), k2.pop(0)
    if   a > b:
        k1.append(b)
        k1.append(a)
    elif a < b:
        k2.append(a)
        k2.append(b)
    if   not k2:
        print turn, 1
        break
    elif not k1:
        print turn, 2
        break
else:
    print -1
