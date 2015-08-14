S = raw_input()
T = raw_input()
for s,t in zip(S,T):
    if s != t:
        if s == "@" and t in "atcoder" or t == "@" and s in "atcoder":
            continue
        else:
            print "You will lose"
            break
else:
    print "You can win"
