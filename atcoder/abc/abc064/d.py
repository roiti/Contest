# -*- coding: utf-8 -*-
def is_correct(s):
    l = 0
    for si in s:
        if si == "(": l += 1
        else: l -= 1
        if l < 0: return False
    return l == 0

N = int(raw_input())
S = raw_input()

flag = False
for i in xrange(105):
    for j in xrange(105):
        T = "("*i + S + ")"*j
        if is_correct(T):
            print T
            flag = True
            break
    if flag:
        break

