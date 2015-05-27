# coding: utf-8
G,C,P = map(int,raw_input().split())
s = raw_input()
g,c,p = s.count("G"),s.count("C"),s.count("P")

ans = 0
ans += 3*(min(g,P)+min(c,G)+min(p,C))
G,C,P,g,c,p = max(0,G-c),max(0,C-p),max(0,P-g),max(0,g-P),max(0,c-G),max(0,p-C)
ans += min(g,G)+min(c,C)+min(p,P)
print ans
