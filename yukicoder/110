Nw = int(raw_input())
W = list(set(map(int,raw_input().split())))
Nb = int(raw_input())
B = list(set(map(int,raw_input().split())))
WB = sorted([[w,"w"] for w in W] + [[b,"b"] for b in B])[::-1]

ans = 0
for sp in range(2):
    bar,col = WB[sp]
    tmp = 1
    for i,wb in WB[sp+1:]:
        if wb != col and i < bar:
            tmp += 1
            col = wb
            bar = i
    ans = max(ans,tmp)
print ans
    