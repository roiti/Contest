# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mod = 10**9 + 7

class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.par = range(size)
        self.g_num = size

    def find(self, x):
        if x == self.par[x]: return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return

        self.g_num -= 1
        if (self.rank[x] > self.rank[y]):
            self.par[y] = x
        else:
            self.par[x] = y
            if (self.rank[x] == self.rank[y]): self.rank[y] += 1

    def group_num(self):
        return self.g_num
#prime = [1] * 1000005
#prime[0] = prime[1] = 0
#for i in xrange(int(1000005**0.5) + 1):
#    if prime[i]:
#        prime[2*i::i] = [0] * len(prime[2*i::i])

p, k = map(int, raw_input().split())
if k == 0:
    print pow(p, p - 1, mod)
    exit()

uf = UnionFind(p)
cnt = 0
for x in xrange(p):
    if x == k*x % p:
        if k > 1:
            cnt += 1
    else:
        uf.unite(x, k*x % p)

ans = pow(p, uf.group_num() - cnt, mod)
print ans
