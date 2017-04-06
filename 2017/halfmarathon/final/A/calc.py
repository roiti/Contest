score = 0
while 1:
    try:
        line = raw_input()
        if line.startswith("score"):
            score += int(line.split(":")[1])
    except:
        break
print score

