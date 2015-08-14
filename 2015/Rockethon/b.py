import itertools
n,m = map(int,raw_input().split())

ls = []
mx = 0
for ele in itertools.permutations(range(1,n+1),n):
    tmp = sum(min(ele[i:j+1]) for i in range(n) for j in range(i,n))
    if tmp == mx:
        ls.append(ele)
    elif tmp > mx:
        mx = tmp
        ls = []
        ls.append(ele)
ls = sorted(ls)
print " ".join(map(str,ls[m-1]))
