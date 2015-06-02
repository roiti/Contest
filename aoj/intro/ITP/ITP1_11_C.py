import random
class Dice:
    def __init__(self, top, front, right, left, back, bottom):
        self.top,   self.bottom = top, bottom
        self.right, self.left   = right, left
        self.front, self.back   = front, back

    def rot(self, d):
        if   d == "N":
            (self.top, self.back, self.bottom, self.front) = (
             self.front, self.top, self.back, self.bottom)
        elif d == "S":
            (self.top, self.back, self.bottom, self.front) = (
             self.back, self.bottom, self.front, self.top)
        elif d == "E":
            (self.top, self.right, self.bottom, self.left) = (
             self.left, self.top, self.right, self.bottom)
        elif d == "W":
            (self.top, self.right, self.bottom, self.left) = (
             self.right, self.bottom, self.left, self.top)

def same(a, b):
    if ((a.top, a.bottom, a.right, a.left, a.front, a.back) ==
        (b.top, b.bottom, b.right, b.left, b.front, b.back)):
        return True
    else:
        return False

ref = {}
ls1 = map(int, raw_input().split())
ls2 = map(int, raw_input().split())
dice1 = Dice(ls1[0], ls1[1], ls1[2], ls1[3], ls1[4], ls1[5])
dice2 = Dice(ls2[0], ls2[1], ls2[2], ls2[3], ls2[4], ls2[5])
for i in xrange(1000):
    d = "NSEW"[random.randint(0,3)]
    dice1.rot(d)
    if same(dice1, dice2):
        print "Yes"
        break
else:
    print "No"
