sa, ya, xa = raw_input().split()
sb, yb, xb = raw_input().split()
if ya == yb:
    print -1
else:
    if   len(ya) > len(yb): print sa
    elif len(ya) < len(yb): print sb
    else:
        for ca, cb in zip(ya, yb):
            if ca > cb:
                print sa
                break
            if ca < cb:
                print sb
                break