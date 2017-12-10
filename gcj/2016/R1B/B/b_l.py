# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

T = int(raw_input())
for case in xrange(T):
    C, J = map(list, raw_input().split())
    N = len(C)
    for i in xrange(N):
        if i < N - 1:
            if C[i] == "?" and J[i] == "?":
                if (C[i + 1] == "?" or J[i + 1] == "?"):
                    C[i] = J[i] = "0"
                else:
                    mn = 100
                    for x in xrange(10):
                        for y in xrange(10):
                            X = "".join(C[:i]) + str(x) + C[i + 1]
                            Y = "".join(J[:i]) + str(y) + J[i + 1]
                            if abs(int(X) - int(Y)) < mn:
                                mn = abs(int(X) - int(Y))
                                C[i] = str(x)
                                J[i] = str(y) 
            elif C[i] == "?":
                if C[i + 1] == J[i + 1]:
                    C[i] = J[i]
                else:
                    mn = 100
                    for x in xrange(10):
                        X = int("".join(C[:i]) + str(x))
                        Y = int("".join(J[:i]) + J[i])
                        if abs(X - Y) < mn:
                            mn = abs(X - Y)
                            C[i] = str(x)
            elif J[i] == "?":
                if C[i + 1] == J[i + 1]:
                    J[i] = C[i]
                else:
                    mn = 100
                    for y in xrange(10):
                        X = int("".join(C[:i]) + C[i])
                        Y = int("".join(J[:i]) + str(y))
                        if abs(X - Y) < mn:
                            mn = abs(X - Y)
                            J[i] = str(x)
        else:
            mn = 1e20
            if C[i] == "?" and J[i] == "?":
                for x in xrange(10):
                    for y in xrange(10):
                        X = int("0" + "".join(C[:-1]))*10 + x
                        Y = int("0" + "".join(J[:-1]))*10 + y
                        if abs(X - Y) < mn:
                            mn = abs(X - Y)
                            C[i] = str(x)
                            J[i] = str(y)
            elif C[i] == "?":
                for x in xrange(10):
                    X = int("0" + "".join(C[:-1]))*10 + x
                    Y = int("".join(J))
                    if abs(X - Y) < mn:
                        mn = abs(X - Y)
                        C[i] = str(x)
            elif J[i] == "?":
                for y in xrange(10):
                    X = int("".join(C))
                    Y = int("0" + "".join(J[:-1]))*10 + y
                    if abs(X - Y) < mn:
                        mn = abs(X - Y)
                        J[i] = str(y)


    C, J = "".join(C), "".join(J)
    print "Case #%d: %s %s" % (case + 1, C, J)
