A, B, C, D, E, F = map(int, raw_input().split())

mx = 0
mx_x = 100*A
mx_y = 0
for i in xrange(31):
    for j in xrange(16):
        if i + j == 0 or 100*A*i + 100*B*j >= F: continue
        for k in xrange(101):
            for l in xrange(51):
                if 100*A*i + 100*B*j + C*k + D*l > F: continue
                if (A*i + B*j)*E < C*k + D*l: continue
                a = 100*A*i + 100*B*j
                b = C*k + D*l
                if 100.0*b/(a + b) > mx:
                    mx_x = a + b
                    mx_y = b
                    mx = 100.0*b/(a + b)
print mx_x, mx_y
