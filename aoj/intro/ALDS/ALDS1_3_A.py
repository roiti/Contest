inp = map(str, raw_input().split())
s = []
for i in inp:
    if   i == "+": s.append( s.pop(-2) + s.pop(-1) )
    elif i == "-": s.append( s.pop(-2) - s.pop(-1) )
    elif i == "*": s.append( s.pop(-2) * s.pop(-1) )
    else: s.append(int(i))
print s[0]


