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

ls = map(int, raw_input().split())
dice = Dice(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5])
for d in raw_input():
    dice.rot(d)
print dice.top
