s = raw_input()
sharp = s.count("#")
s = s.replace("#",")",sharp-1)
need = s.count("(")-s.count(")")
s = s.replace("#",")"*max(1,need))
balance = 0
for i in s:
    if i == "(":
        balance += 1
    else:
        balance -= 1
        if balance < 0:
            print -1
            break
else:
    for i in range(sharp-1):
        print 1
    print need
