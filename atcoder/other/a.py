T = raw_input()
S = B = O = 0
for t in T:
    if t == "S":
        S += 1
        if S == 3:
            O += 1
            S = B = 0
            if O == 3:
                O = 0
    if t == "B":
        B += 1
        if B == 4:
            S = B = 0
print "B" + "o" * B
print "S" + "o" * S
print "O" + "o" * O
