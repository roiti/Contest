hist = [0]*10
l = map(int,raw_input().split())
for li in l: hist[li] += 1
if max(hist) >= 4:
    if hist[min(l)] == 2 or hist[max(l)] == 2 or hist[max(l)] == 6:
        print "Elephant"
    else:
        print "Bear"
else:
    print "Alien"
