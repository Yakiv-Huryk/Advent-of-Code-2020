#!/usr/bin/python3

from numpy import array, radians, cos, sin, int64

def get_input():
    with open('input') as f:
        for l in f.readlines():
            yield {'action': l[0], 'value': int(l[1:])}

dirs = {
    'N': array([[0], [1]]),
    'S': array([[0], [-1]]),
    'E': array([[1], [0]]),
    'W': array([[-1], [0]])
}

def solve(commands, wp_mode, wp_start):
    wp = wp_start
    pos = array([[0], [0]])
    for c in commands:
        action = c['action']
        if action in dirs:
            if wp_mode:
                wp += dirs[action] * c['value']
            else:
                pos += dirs[action] * c['value']
        elif action == 'R' or action == 'L':
            angle = c['value'] if action == 'L' else 360 - c['value']
            r = radians(angle)
            c, s = cos(r), sin(r)
            rm = array(((c, -s), (s, c))).astype(int64)
            wp = rm.dot(wp)
        else:
            pos += wp * c['value']
    return abs(pos[0][0]) + abs(pos[1][0])

d = list(get_input())
p1 = solve(d, wp_mode=False, wp_start=dirs['E'])
print(f'Part1: {p1}')
p2 = solve(d, wp_mode=True, wp_start=dirs['E']*10 + dirs['N'])
print(f'Part2: {p2}')
