#!/usr/bin/python3

import re


def parse_pass(s):
    info = {}
    for f in s.replace('\n', ' ').split(' '):
        k, v = f.split(':')
        info[k] = v
    return info


def get_passports():
    passports = []
    with open('./input') as f:
        for p in f.read().split('\n\n'):
            passports.append(parse_pass(p))
    return passports


def hgt_filter(x):
    num, m = x[:len(x)-2], x[len(x)-2:]
    if m == 'cm':
        return int(num) in range(150, 193 + 1)
    if m == 'in':
        return int(num) in range(59, 76 + 1)
    return False


required = {
    'byr': lambda x: int(x) in range(1920, 2002 + 1),
    'iyr': lambda x: int(x) in range(2010, 2020 + 1),
    'eyr': lambda x: int(x) in range(2020, 2030 + 1),
    'hgt': hgt_filter,
    'hcl': lambda x: re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9 and int(x)
}

valid_part_1 = 0
valid_part_2 = 0
for p in get_passports():
    if set(required.keys()).issubset(set(p.keys())):
        valid_part_1 += 1
        is_valid = True
        for rk, rf in required.items():
            if not rf(p[rk]):
                is_valid = False
                break
        if is_valid:
            valid_part_2 += 1

print(f'Valid part 1: {valid_part_1}')
print(f'Valid part 2: {valid_part_2}')
