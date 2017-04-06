# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll, random

def print_board():
    for y in xrange(Y):
        line = ""
        for x in xrange(X):
            line += "#" if board[y][x] else "-"
        print line
    print
    sys.stdout.flush()
            
def is_inside(x, y):
    return 0 <= y < Y and 0 <= x < X

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

Y, X, K, T = map(int, raw_input().split())
car = [map(int, raw_input().split()) for i in xrange(K)]
for i, (y, x, gy, gx) in enumerate(car):
    car[i] = [y - 1, x - 1, gy - 1, gx - 1]

board = [[False]*X for i in xrange(Y)]
for y, x, gy, gx in car:
    board[y][x] = True


def main():
    global board
    moves = []
    for loop in xrange(min(25, T)):
        #print_board()
        move = ""
        _board = copy.deepcopy(board)
        for i, (y, x, gy, gx) in enumerate(car):
            if (y, x) == (gy, gx):
                move += "-"
                continue
            order = [0, 1, 2, 3]
            order.sort(key = lambda j: abs(x + dxy[j][0] - gx) + abs(y + dxy[j][1] - gy))
            for j in order:
                dx, dy = dxy[j]
                nx, ny = x + dx, y + dy
                if not is_inside(nx, ny): continue
                if board[ny][nx]: continue
                if _board[ny][nx]: continue
                _board[ny][nx] = True
                _board[y][x] = False
                move += "RDLU"[j]
                car[i] = [ny, nx, gy, gx]
                break
            else:
                move += "-"
        board = copy.deepcopy(_board)
        moves.append(move)
        assert len(move) == 450

    print len(moves)
    for move in moves:
        print move


if __name__ == "__main__":
    main()
