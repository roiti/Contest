def rec(shift, a):
    if len(a) <= 1: return 0

    one  = [ai ^ (ai & (1 << shift)) for ai in a if     ai & (1 << shift) and ai >> (shift+1) == 0]
    zero = [ai ^ (ai & (1 << shift)) for ai in a if not ai & (1 << shift) and ai >> (shift+1) == 0]
    
    if not zero: return rec(shift - 1,  one)
    if not  one: return rec(shift - 1, zero)

    return (1 << shift) + min(rec(shift - 1, zero), rec(shift - 1, one))

N = int(raw_input())
A = list(set(map(int,raw_input().split())))
print rec(30,A)