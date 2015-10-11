#coding: utf-8
import itertools as it

a = [-1] * 9
memo = {}

def dfs(turn):
    if tuple(a) in memo: return memo[tuple(a)]

    p = [-1, -1]
    for y in xrange(3):
        for x in xrange(3):
            if a[3 * y + x] != -1: continue
            a[3 * y + x] = turn
            res = dfs(1 - turn)
            a[3 * y + x] = -1
            if res[turn] > p[turn]:
                p = res

    if p == [-1, -1]:
        p = [0, 0]
        for y in xrange(2):
            for x in xrange(3):
                if a[y * 3 + x] == a[y * 3 + x + 3]:
                    p[0] += b[y][x]
                else:
                    p[1] += b[y][x]
        for y in xrange(3):
            for x in xrange(2):
                if a[y * 3 + x] == a[y * 3 + x + 1]:
                    p[0] += c[y][x]
                else:
                    p[1] += c[y][x]
    memo[tuple(a)] = p
    return p

b = [map(int, raw_input().split()) for i in xrange(2)]
c = [map(int, raw_input().split()) for i in xrange(3)]
p = dfs(0)
print p[0]
print p[1]
