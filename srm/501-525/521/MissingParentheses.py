# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class MissingParentheses:
    def countCorrections(self, par):
        return countCorrections(par)

def countCorrections(par):
    for i in xrange(1000):
        par = par.replace("()", "")
    return len(par)

