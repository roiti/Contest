W,D = int(raw_input()),int(raw_input())
for d in range(D,1,-1):
    W -= W/d**2
print W