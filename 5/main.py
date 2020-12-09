#!/usr/bin/python3

def convert(ps):
    num = ps.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(num, 2)

def get_seats():
    with open('./input') as f:
        seats = []
        for ps in f.readlines():
            ps = ps.strip()
            seats.append(convert(ps))
    return seats

def find_seat(seats):
    for s in range(int('1000', 2), max(seats)):
        if (s not in seats) and (s + 1 in seats) and (s - 1 in seats):
            return s

seats = get_seats()
print(f'Part1 max = {max(seats)}')
print(f'Part2 seat = {find_seat(seats)}')


