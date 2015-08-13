# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

inf = 10000000
class LuckyCycle:
    def getEdge(self, e1, e2, w):
        e1 = [i - 1 for i in e1]
        e2 = [i - 1 for i in e2]
        N = len(e1)

        d = [[inf] * (N + 1) for i in xrange(N + 1)]
        for i in xrange(N):
            d[e1[i]][e2[i]] = d[e2[i]][e1[i]] = (1 if w[i] == 4 else 1000)

        for k in xrange(N + 1):
            for i in xrange(N + 1):
                for j in xrange(N + 1):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        for i in xrange(N + 1):
            for j in xrange(i + 1, N + 1):
                if d[i][j] == 1 or d[i][j] == 1000: continue
                four, seven = d[i][j] % 1000, d[i][j] / 1000
                if abs(four - seven) == 1:
                    add = 7 if four - seven == 1 else 4
                    return (i + 1, j + 1, add)
            
        return ()

