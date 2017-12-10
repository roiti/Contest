# -*- coding: utf-8 -*-
import sys

remain = 64

N = raw_input()

def query(n):
    global remain
    print "? " + str(n)
    sys.stdout.flush()
    remain -= 1
    if N:
        if int(n) <= int(N) and str(n) <= str(N):
            return True
        if int(N) < int(n) and str(N) < str(n):
            return True
        return False
    return raw_input() == "Y"

def answer(n):
    print "! " + str(n)
    sys.stdout.flush()
    exit()


def solve():
    ans = query("9"*8)
    if not ans:
        answer(10**9)

    L = 7
    while (remain and L > 1):
        if query("1" + "0"*(L - 1)):
            break
        L -= 1

    if L == 1:
        for i in xrange(1, 10):
            if query(i) and query(10*i):
                answer(i)

    n = "" 
    while (remain and len(n) < L - 1):
        k = 5
        while True:
            m = n + str(k)
            ans = query(m)
            if ans:
                if k >= 5:
                    k += 1
                else:
                    n += str(k) 
                    break
            if not ans:
                if k <= 5:
                    k -= 1
                else:
                    n += str(k - 1)
                    break
            if k == -1:
                n += "0"
                break
            if k == 10:
                n += "9"
                break

    for i in xrange(10):
        if query(n + str(i) + "0"):
            answer(n + str(i))

solve()
