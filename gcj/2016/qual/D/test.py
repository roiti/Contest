import itertools

K, C = map(int, raw_input().split())
for tile in itertools.product("GL", repeat = K):
    tile = "".join(tile)
    result = tile
    for i in xrange(C):
        result = "".join([tile if c == "L" else "G"*K for c in result])
    #print tile, ":", result
