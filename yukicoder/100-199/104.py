S = raw_input()
road = 1
for s in S:
    if s == "L":
        road = 2*road
    elif s == "R":
        road = 2*road+1
print road