from math import *
A, B = map(float, raw_input().split())
if A > B: A, B = B, A
diag = sqrt(A * A + B * B)
atanAB = atan2(A, B)

N = int(raw_input())
for loop in xrange(N):
    C, D = map(float, raw_input().split())
    if C > D: C, D = D, C
    if A > C:
        print "NO"
        continue
    elif A <= C and B <= D:
        print "YES"
        continue

    a = asin(D / diag)
    theta = a - 2 * atanAB
    if diag * cos(theta) <= C:
        print "YES"
    else:
        print "NO"
