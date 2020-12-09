#!/usr/bin/python3

with open('./input') as f:
    valid_part_1 = 0
    valid_part_2 = 0
    for l in f.readlines():
        policy, psw = l.split(':')
        psw = psw.strip()

        minmax, c = policy.split(' ')
        rmin, rmax = [*map(int, minmax.split('-'))]

        if psw.count(c) in range(rmin, rmax + 1):
            valid_part_1 += 1
        if (psw[rmin-1] == c) ^ (psw[rmax-1] == c):
            valid_part_2 += 1

    print(f'Valid count count part1: {valid_part_1}')
    print(f'Valid count count part2: {valid_part_2}')
