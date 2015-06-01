while 1:
    n = int(raw_input())
    if n == 0: break
    steps = raw_input().split()
    lr = [0,0]
    start = 0
    ans = 0
    for step in steps:
        if step[0] == "l":
            if step[1] == "u": lr[0] += 1
            else: lr[0] -= 1
        else:
            if step[1] == "u": lr[1] += 1
            else: lr[1] -= 1
        if (lr == [1,1] and start == 0) or (lr == [0,0] and start == 1):
            ans += 1
            start = lr[0]
    print ans

