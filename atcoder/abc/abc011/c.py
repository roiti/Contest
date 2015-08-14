N = int(raw_input())
NG = sorted([int(raw_input()) for _ in range(3)])
for roop in range(100):
    if N in NG:
        print "NO"
        break
    if   N-3 >= 0 and N-3 not in NG: N -= 3
    elif N-2 >= 0 and N-2 not in NG: N -= 2
    elif N-1 >= 0 and N-1 not in NG: N -= 1
    else:
        print "NO"
        break
    if N == 0:
        print "YES"
        break
else:
    print "NO"
