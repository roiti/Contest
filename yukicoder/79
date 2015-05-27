N = int(raw_input())
poll = [0]*6
for i in map(int,raw_input().split()):
    poll[i-1] += 1
mx = max(poll)
for i in range(6-1,-1,-1):
    if poll[i] == mx:
        print i+1
        break
