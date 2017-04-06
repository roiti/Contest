# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

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
        cost = 99
        if s == D:
            return used
        if i >= N:
            return []
        if s + C[i] <= D:
            x_list = dfs(i + 1, s + C[i], used + [i])
            if x_list:
                tmp = 0
                for x in x_list:
                    if A[x] == 0:
                        tmp += 1
                if tmp < cost:
                    cost = tmp
                    res = x_list
        x_list = dfs(i + 1, s, used)
        if x_list:
            tmp = 0
            for x in x_list:
                if A[x] == 0:
                    tmp += 1
            if tmp < cost:
                cost = tmp
                res = x_list
        return res

    D, T = map(int, raw_input().split())
    C = map(int, raw_input().split())
    A = map(int, raw_input().split())

    x_list = dfs(0, 0, [])

    if x_list:
        cost = sum(x for x in x_list if A[x] == 0) 
        if cost == 0:
            sell(x_list)
            return
        if cost < T:
            for x in x_list:
                if A[x] == 0:
                    fill(x)
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
