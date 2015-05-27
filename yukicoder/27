import itertools as it
V = map(int,raw_input().split())

ans = 1000
for a,b,c in it.product(range(1,31),repeat = 3):
    tmp = 0
    for Vi in V:
        need = 1000
        for i in range(31):
            for j in range(31):
                rem = Vi-i*a-j*b
                if rem < 0: break
                if rem%c == 0:
                    need = min(need,i+j+rem/c)
        tmp += need
    ans = min(ans, tmp)
print ans
