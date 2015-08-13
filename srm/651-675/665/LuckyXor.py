# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class LuckyXor:
    def construct(self, a):
        return construct(a)

def construct(a):
    lucky = [4, 7, 44, 47, 74, 77]
    for b in xrange(a + 1, 101):
        if a ^ b in lucky:
            return b
    return -1

