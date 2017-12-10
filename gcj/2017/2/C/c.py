# -*- coding: utf-8 -*-
IMPOSSIBLE = "IMPOSSIBLE"
POSSIBLE = "POSSIBLE"

T = int(raw_input())

def hit():
    hitted = set()
    for r in xrange(R):
        for c in xrange(C):
            if A[r][c] == "-":
                for cc in xrange(c + 1, C):
                    if A[r][cc] == ".":
                        hitted.add((r, cc))
                    elif A[r][cc] == "#":
                        break
                for cc in xrange(c - 1, -1, -1):
                    if A[r][cc] == ".":
                        hitted.add((r, cc))
                    elif A[r][cc] == "#":
                        break
            if A[r][c] == "|":
                for rr in xrange(r + 1, R):
                    if A[rr][c] == ".":
                        hitted.add((rr, c))
                    elif A[rr][c] == "#":
                        break
                for rr in xrange(r - 1, -1, -1):
                    if A[rr][c] == ".":
                        hitted.add((rr, c))
                    elif A[rr][c] == "#":
                        break
    for r in xrange(R):
        for c in xrange(C):
            if A[r][c] == ".":
                if (r, c) not in hitted:
                    return False
    return True

def solve():
    must_v = set()
    must_h = set()

    g = []
    for r in xrange(R):
        for c in xrange(C):
            a = A[r][c]
            if a in ["#", "/", "\\"]:
                if len(g) > 1:
                    for xy in g:
                        must_v.add(xy)
                g = []
            elif a in ["-", "|"]:
                g.append((r, c))
        
        if len(g) > 1:
            for rc in g:
                must_v.add(rc)
        g = []

    for c in xrange(C):
        for r in xrange(R):
            a = A[r][c]
            if a in ["#", "/", "\\"]:
                if len(g) > 1:
                    for xy in g:
                        must_h.add(xy)
                g = []
            elif a in ["-", "|"]:
                g.append((r, c))
        
        if len(g) > 1:
            for rc in g:
                must_h.add(rc)
        g = []

    for rc in must_v:
        if rc in must_h:
            return False 
    
    for r,c in must_v:
        A[r][c] = "|"
    for r,c in must_h:
        A[r][c] = "-"
         
    return hit()

for case in xrange(1, T ++ 1):
    R, C = map(int, raw_input().split())
    A = [list(raw_input()) for i in xrange(R)]
    if solve():
        print "Case #%d: %s" % (case, POSSIBLE)
        for line in A:
            print "".join(line)
    else:
        print "Case #%d: %s" % (case, IMPOSSIBLE)
