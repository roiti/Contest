A = [map(int, raw_input().split()) for i in xrange(4)]

over = True
for i in xrange(4):
    for j in xrange(3):
        if A[i][j] == A[i][j + 1]:
            over = False
            break
        if A[j][i] == A[j + 1][i]:
            over = False
            break

print "GAMEOVER" if over else "CONTINUE"
