import math
while True:
    n = int(raw_input())
    if n == 0:
        break
    stdnt = map(int, raw_input().split())
    ave = 0
    for score in stdnt:
        ave += float(score)/n
    alpha = 0
    for score in stdnt:
        alpha += (score-ave) ** 2/n
    print math.sqrt(alpha)
    

