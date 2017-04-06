# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll, random

N = 8
LOOP = 1000
MIN_D = 1
MAX_D = 50
MIN_T = 1
MAX_T = 50


def flush(s):
    print s
    sys.stdout.flush()

def fill(i):
    flush("fill %d" % (i + 1))

def move(i, j):
    flush("move %d %d" % (i + 1, j + 1))

def change(i):
    flush("change %d" % (i + 1))

def pazz():
    flush("pass")

def sell(x_list):
    n = len(x_list)
    s = "sell %d" % n
    for x in x_list:
        s += " %d" % (x + 1)
    flush(s)

def do():
    def dfs(i, s, used):
        res = []
        if s == D:
            return used
        if i >= N:
            return []
        if A[i] > 0 and s + A[i] <= D:
            x_list = dfs(i + 1, s + A[i], used + [i])
            if len(x_list) > len(res):
                res = x_list
        x_list = dfs(i + 1, s, used)
        if len(x_list) > len(res):
            res = x_list
        return res

    D, T = map(int, raw_input().split())
    C = map(int, raw_input().split())
    A = map(int, raw_input().split())

    x_list = dfs(0, 0, [])

    if x_list:
        sell(x_list)
        return

    mn, idx = 99, 0

    for i, a in enumerate(A):
        if a == 0 and C[i] < mn:
            mn = C[i]
            idx = i
    if mn < 99:
        fill(idx)
        return

    if sum(C) < 50:
        mn = min(C)
        for i, c in enumerate(C):
            if c == mn:
                change(i)
                return

    pazz()
    return

def main():
    for loop in xrange(LOOP):
        do()

if __name__ == "__main__":
    main()
