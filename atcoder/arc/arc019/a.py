trans = zip("ODIZSB", "001258")
S = raw_input()
for b, a in trans:
    S = S.replace(b, a)
print S
