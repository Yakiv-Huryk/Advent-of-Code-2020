#!/usr/bin/python3


def get_input():
    with open('input') as f:
        return list(map(int, f.readlines()))


def solve_1(l):
    d = [0] * 4
    for i in range(1, len(l)):
        diff = l[i] - l[i - 1]
        d[diff] += 1
    return d[1] * d[3]

def solve_2(l):
    d = [0] * len(l)
    d[-1] = 1
    for i in reversed(range(0, len(l))):
        for x in range(1, 4):
            if i + x + 1 > len(l):
                continue
            if l[i + x] - l[i] < 4:
                d[i] += d[i + x]
    return d[0]
        

l = sorted(get_input())
l = [0] + l + [max(l) + 3]
p1 = solve_1(l)
print(f'Part1: {p1}')
p2 = solve_2(l)
print(f'Part2: {p2}')
