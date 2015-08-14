r, s, p = map(int, raw_input().split())
prob = [[[0.0] * 110 for i in xrange(110)] for j in xrange(110)]
prob[r][s][p] = 1.0
for i in xrange(r, -1, -1):
    for j in xrange(s, -1, -1):
        for k in xrange(p, -1, -1):
            if k > 0: prob[i][j][k] += prob[i + 1][j][k] * (i + 1) * k / ((i + 1) * k + j * k + (i + 1) * j)
            if i > 0: prob[i][j][k] += prob[i][j + 1][k] * (j + 1) * i/ ((j + 1) * i + i * k + (j + 1) * k)
            if j > 0: prob[i][j][k] += prob[i][j][k + 1] * (k + 1) * j/ ((k + 1) * j + i * (k + 1) + i * j)
            
print "%.12f %.12f %.12f" % (sum(prob[i][0][0] for i in xrange(1, r + 1)),
                            sum(prob[0][i][0] for i in xrange(1, s + 1)),
                            sum(prob[0][0][i] for i in xrange(1, p + 1)))
