N = int(raw_input())
c = raw_input()
s = "b"
for i in xrange(102):
    if s == c:
        print i
        break
    if i % 3 == 0: s = "a" + s + "c"
    elif i % 3 == 1: s = "c" + s + "a"
    elif i % 3 == 2: s = "b" + s + "b"
else:
    print -1
