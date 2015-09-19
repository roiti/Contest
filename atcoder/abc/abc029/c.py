import itertools as it
N = int(raw_input())
for password in it.product("abc", repeat = N):
    print "".join(password)

