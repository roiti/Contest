n = int(raw_input())
a = [raw_input() for _ in range(n)]
poll = {i:0 for i in set(a)}
for i in a: poll[i] += 1
ans,mx = "",0
for key,val in poll.items():
    if val > mx:
        ans,mx = key,val
print ans
