N = int(raw_input())
for i in xrange(3, int(N**0.5) + 3):
    if N%i == 0:
        print i
        break
else:
    print N if N%2 else N/2

