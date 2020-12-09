#!/usr/bin/python3

from pprint import pprint

def parse_input():
    with open('./input') as f:
        data = {}
        for l in f.readlines():
            a, b = l.strip().split('contain')
            k = a.split('bags')[0].strip()
            data[k] = {'values': [], 'checked': False, 'gold': False, 'len': 0}
            if b != ' no other bags.':
                for v in b.split(','):
                    v = v.strip()
                    name = ' '.join(v.split(' ')[1:3])
                    count = int(v.split(' ')[0])
                    data[k]['values'].append({'name': name, 'count': count})
        return data

def check_bag(data, bug):
    if data[bug]['checked']:
        return

    data[bug]['checked'] = True

    if 'shiny gold' in [v['name'] for v in data[bug]['values']]:
        data[bug]['gold'] = True

    for b in data[bug]['values']:
        check_bag(data, b['name'])
        data[bug]['gold'] |= data[b['name']]['gold']
        data[bug]['len'] += b['count'] * (data[b['name']]['len'] + 1)


data = parse_input()
for k in data.keys():
    check_bag(data, k)

p1 = len([*filter(lambda x: x['gold'], data.values())])
p2 = data['shiny gold']['len']

print(f'Part1: {p1}')
print(f'Part2: {p2}')
