d = int(raw_input())
_H1, _H2, _H3 = int(raw_input()), int(raw_input()), int(raw_input())

if d == 0:
    if _H1 != _H3 and (_H1 < _H2 > _H3 or _H1 > _H2 < _H3):
        print 0
    else:
        print -1
    exit()

ans = -1
a1 = a2 = 0
H1, H2, H3 = _H1, _H2, _H3
if H1 >= H2:
    c = (H1 - H2 + d) / d
    H1 = max(0, H1 - d * c)
    a1 += c
if H3 >= H2:
    c = (H3 - H2 + d) / d
    H3 = max(0, H3 - d * c)
    a1 += c
if H1 == H3:
    H1 = max(0, H1 - d)
    a1 += 1
if H1 != H3 and H1 < H2 > H3:
    ans = a1

H1, H2, H3 = _H1, _H2, _H3
if H1 <= H2:
    c = (H2 - H1 + d) / d
    H2 = max(0, H2 - d * c)
    a2 += c
if H3 <= H2:
    c = (H2 - H3 + d) / d
    H2 = max(0, H2- d * c)
    a2 += c
if H1 == H3:
    H1 = max(0, H1 - d)
    a2 += 1
if H1 == H2:
    H2 = max(0, H2 - d)
    a2 += 1
if H1 != H3 and H1 > H2 < H3:
    if ans == -1: ans = a2
    else: ans = min(ans, a2)
print ans

