#!/usr/bin/python3

from copy import deepcopy

def get_input():
    with open('input') as f:
        d = []
        for l in f.readlines():
            d.append(['.'] + list(l.strip()) + ['.'])
        d = [['.'] * len(d[0])] + d
        d.append(['.'] * len(d[0]))
        return d

def neighbors(d, x, y):
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            if xi == x and yi == y:
                continue
            yield xi, yi

def neighbors_ray(d, x, y):
    for dx, dy in [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]:
        k = 1
        while True:
            xx = x + dx * k
            yy = y + dy * k
            if  xx < 0 or yy < 0:
                break
            if xx >= len(d) or yy >= len(d[0]):
                break
            if d[xx][yy] != '.':
                yield xx, yy
                break
            k += 1

def morph(d, db, x, y, get_neighbors, occ_limit):
    v = d[x][y]
    occupied = len([(xi, yi) for xi, yi in get_neighbors(d, x, y) if d[xi][yi] == '#'])
    if v == 'L':
        if occupied == 0:
            db[x][y] = '#'
            return True
    if v == '#' and occupied >= occ_limit:
        db[x][y] = 'L'
        return True
    return False

def solve(d, get_neighbors, occ_limit):
    changed = True
    while changed:
        db = deepcopy(d)
        changed = False
        for x in range(1, len(d) - 1):
            for y in range(1, len(d[x]) - 1):
                changed |= morph(d, db, x, y, get_neighbors, occ_limit)
        d = db
    return sum([l.count('#') for l in d])

d = get_input()
p1 = solve(d, neighbors, occ_limit=4)
print(f'Part1: {p1}')
p2 = solve(d, neighbors_ray, occ_limit=5)
print(f'Part2: {p2}')
