import random
class Dice:
    def __init__(self, ls):
        self.top,   self.bottom = ls[0], ls[5]
        self.right, self.left   = ls[2], ls[3]
        self.front, self.back   = ls[1], ls[4]

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

    def show(self):
        return (self.top, self.bottom, self.right,
                self.left, self.front, self.back)

S = set()
N = int(raw_input())
judge = True
for i in xrange(N):
    dice = Dice(map(int, raw_input().split()))
    s = set()
    for loop in xrange(1000):
        nums = dice.show()
        if nums in S:
            judge = False
            break
        s.add(nums)
        dice.rot("NSEW"[random.randint(0, 3)])
    if not judge:
        break
    S |= s
print "Yes" if judge else "No"
