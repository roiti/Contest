# -*- coding: utf-8 -*-
IMPOSSIBLE = "IMPOSSIBLE"

def solve():
    N, R, O, Y, G, B, V = map(int, raw_input().split()) 
    if R == G and R + G == N: return "RG"*G
    if Y == V and Y + V == N: return "YV"*V
    if O == B and O + B == N: return "BO"*O
    if (G and G >= R) or (V and V >= Y) or (O and O >= B): return IMPOSSIBLE

    R -= G; Y -= V; B -= O;
    M = R + Y + B
    mx = max(R, Y, B)

    if 2*mx > M: return IMPOSSIBLE

    ans = [""]*M
    I, J, K = sorted([[R, "R"], [Y, "Y"], [B, "B"]], reverse = True)
    for i in xrange(0, M, 2):
        if   I[0]: ans[i] = I[1]; I[0] -= 1
        elif J[0]: ans[i] = J[1]; J[0] -= 1
        elif K[0]: ans[i] = K[1]; K[0] -= 1
    for i in xrange(1, M, 2):
        if   J[0]: ans[i] = J[1]; J[0] -= 1
        elif K[0]: ans[i] = K[1]; K[0] -= 1
        elif I[0]: ans[i] = I[1]; I[0] -= 1

    ans = "".join(ans)
    if O: ans = ans.replace("B", "BO"*O + "B", 1)
    if G: ans = ans.replace("R", "RG"*G + "R", 1)
    if V: ans = ans.replace("Y", "YV"*V + "Y", 1)

    assert len(ans) == N
    return "".join(ans)

T = int(raw_input())
for case in xrange(1, T + 1):
    print "Case #%d: %s" % (case, solve())

