#!/usr/bin/python3

from string import ascii_lowercase

with open('./input') as f:
        part1 = 0
        part2 = 0
        for group in f.read().split('\n\n'):
            union = set()
            inter = set(ascii_lowercase)
            for p in group.split('\n'):
                union |= set(p)
                inter = inter.intersection(set(p))
            part1 += len(union)
            part2 += len(inter)
        
        print(f'Part1: {part1}')
        print(f'Part2: {part2}')
