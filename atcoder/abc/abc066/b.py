S = raw_input()
n = len(S)
for i in xrange(1, n):
    if (n - i)%2 > 0: continue
    T = S[:-i]
    if T[:len(T)/2] == T[len(T)/2:]:
        print n - i
        break

