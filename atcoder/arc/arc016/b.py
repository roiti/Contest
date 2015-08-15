N = int(raw_input())
bx = "." * 9
ans = 0
for i in xrange(N):
    x = raw_input()
    for j in xrange(9):
        if x[j] == bx[j] == "o": continue
        elif x[j] == "o": ans += 1
        elif x[j] == "x": ans += 1
    bx = x
print ans

        
