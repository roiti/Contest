x0,y0,x1,y1,x2,y2 = map(int,raw_input().split())
flag = False
for x in range(-200,201):
    for y in range(-200,201):
        xy = [[x0,y0],[x1,y1],[x2,y2],[x,y]]
        d = [(xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2 for i in range(4) for j in range(i+1,4)]
        if len(set(d)) == 2:
            print x,y
            flag = True
            break
    if flag: break
else:
    print -1