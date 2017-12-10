# -*- coding: utf-8 -*-
import copy

def is_snake(x, y):
    B = copy.deepcopy(A)
    while True:
        B[y][x] = "@"
        if B[1 - y][x] == "#":
            x, y = x, 1 - y 
        elif x + 1 < n and B[y][x + 1] == "#":
            x, y = x + 1, y
        else:
            break

    for i in xrange(n):
        if B[0][i] == "#" or B[1][i] == "#":
            return False
    return True

T = int(raw_input())
for loop in xrange(T):
    n = int(raw_input())
    A = [list(raw_input()) for i in xrange(2)]

    ans = False
    flag = False
    for i in xrange(n):
        if A[0][i] == "#":
            x, y = i, 0
            ans |= is_snake(i, 0) 
            flag = True
        if A[1][i] == "#":
            x, y = i, 1
            ans |= is_snake(i, 1)
            flag = True
        if flag: break

    print "yes" if ans else "no"
    
