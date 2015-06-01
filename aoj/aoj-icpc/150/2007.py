coins = (10,50,100,500)
isfirst = True
while 1:
    cost = int(raw_input())
    if cost == 0: break
    if not isfirst: print
    have = map(int,raw_input().split())

    budget = sum(i*j for i,j in zip(coins,have))
    change = budget-cost

    ret = [0]*4
    for i in reversed(range(4)):
        c = change/coins[i]
        ret[i] = c
        change -= c*coins[i]

    for i in range(4):
        if have[i]-ret[i] <= 0: continue
        print coins[i],have[i]-ret[i]

    isfirst = False

