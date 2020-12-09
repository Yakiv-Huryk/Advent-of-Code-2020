#!/usr/bin/python3

def get_forest():
    forest = []
    with open('./input') as f:
        for l in f.readlines():
            forest.append(*l.split())
    return forest

def index_generator(dx, dy, xmax, ymax):
    x = 0
    y = 0
    while x < xmax:    
        yield x, y
        x += dx
        y = (dy + y) % ymax

def solve_for_dx_dy(forest, dx, dy):
    trees = 0
    gen = index_generator(dx, dy, len(forest), len(forest[0]))
    try:
        while True:
            x, y = next(gen)
            if forest[x][y] == '#':
                trees += 1
    except:
        print(f'Trees Right {dy} Down {dx} {trees}')  # 164
        return trees

forest = get_forest()

r1=solve_for_dx_dy(forest, 1, 1)
r2=solve_for_dx_dy(forest, 1, 3)
r3=solve_for_dx_dy(forest, 1, 5)
r4=solve_for_dx_dy(forest, 1, 7)
r5=solve_for_dx_dy(forest, 2, 1)

print(f'Part1: {r2}')
print(f'Part2: {r1 * r2 * r3 * r4 * r5}')
