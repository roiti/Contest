while True:
    line = map(int, raw_input().split())
    if line[0] == 0 and line[1] == 0:
        break
    line.sort()
    print line[0],line[1]

