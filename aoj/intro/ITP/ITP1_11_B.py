import random
class Dice:
    def __init__(self, top, front, right, left, back, bottom):
        self.top,   self.bottom = top, bottom
        self.right, self.left   = right, left
        self.front, self.back   = front, back

    def rot(self, d):
        if   d == "N":
            self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom
        elif d == "S":
            self.top, self.back, self.bottom, self.front = self.back, self.bottom, self.front, self.top
        elif d == "E":
            self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom
        elif d == "W":
            self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top

ref = {}
ls = map(int, raw_input().split())
dice = Dice(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5])
for i in xrange(1000):
    d = "NSEW"[random.randint(0,3)]
    dice.rot(d)
    ref[(dice.top, dice.front)] = dice.right

for i in xrange(input()):
    a, b = map(int, raw_input().split())
    print ref[(a, b)]
