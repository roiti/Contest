import itertools as it
class mybool:
    def __init__(self, value):
        self.value = value
    def __neg__(self):
        return mybool(2-self.value)
    def __mul__(self, other):
        return mybool(min(self.value,other.value))
    def __add__(self, other):
        return mybool(max(self.value,other.value))

while 1:
    s = raw_input()
    if s == ".": break

    for i in xrange(3):
        s = s.replace(str(i),"mybool(%d)"%i)
    
    ans = 0
    for p,q,r in it.product([0,1,2],repeat=3):
        P,Q,R = mybool(p),mybool(q),mybool(r)
        if eval(s).value == 2:
            ans += 1
    
    print ans
    

