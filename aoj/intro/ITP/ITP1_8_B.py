while True:
    x = str(raw_input())
    if int(x) == 0:
        break
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    print sum


