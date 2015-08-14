import itertools
N = int(raw_input())
xy = [map(int,raw_input().split()) for _ in range(N)]
ans = 0
for xy1,xy2,xy3 in itertools.combinations(xy,3):
    ax,ay = xy1; bx,by = xy2; cx,cy = xy3
    s = abs(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))
    if s > 0 and s%2 == 0: ans += 1
print ans
