#!/usr/bin/python3

def part1(numbers):
    for a in numbers:
        b = 2020 - a
        try:
            numbers.index(b)
        except:
            continue
        print(f'{a} * {b} = {a * b}')
        return


def part2(numbers):
    for ai in range(len(numbers)):
        a = numbers[ai]
        for bi in range(ai, len(numbers)):
            b = numbers[bi]
            c = 2020 - a - b
            try:
                numbers[bi:].index(c)
            except:
                continue
            print(f'{a} * {b} * {c} = {a * b * c}')


with open('./input') as f:
    numbers = [*map(int, f.readlines())]

part1(numbers)
part2(numbers)


    



