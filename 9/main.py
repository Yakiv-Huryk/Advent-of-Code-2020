#!/usr/bin/python3

def get_input():
    with open('input') as f:
        return list(map(int, f.readlines()))


def find_sum(v, l):
    for ai, a in enumerate(l):
        for bi, b in enumerate(l):
            if ai == bi:
                continue
            if a + b == v:
                return True
    return False


def solve_1(v, pl=25):
    for i in range(pl, len(v)):
        if not find_sum(v[i], v[i-pl:i]):
            return v[i]


def solve_2(l, v):
    b = 0
    e = 1
    s = l[0] + l[1]
    while e < len(l):
        #print(f'{b} {e} sum {s} {l[b:e+1]}')
        if s == v:
            return min(l[b:e+1]) + max(l[b:e+1])
        if (b + 1 == e) or s < v:
            e += 1
            s += l[e]
        else:
            s -= l[b]
            b += 1
    return None


l = get_input()
p1 = solve_1(l)
print(f'Part1: {p1}')
p2 = solve_2(l, p1)
print(f'Part2: {p2}')
