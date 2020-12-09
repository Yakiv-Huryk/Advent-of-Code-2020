#!/usr/bin/python3

from copy import deepcopy

def get_cmds():
    cmds = []
    with open('./input') as f:
        for l in f.readlines():
            cmd, op = l.strip().split(' ')
            cmds.append({'cmd': cmd, 'op': int(op), 'used': False})
    return cmds

def nop(ctx, op):
    ctx['trace'].append(ctx['ip'])
    ctx['ip'] += 1

def acc(ctx, op):
    ctx['acc'] += op 
    ctx['ip'] += 1

def jmp(ctx, op):
    ctx['trace'].append(ctx['ip'])
    ctx['ip'] += op

code = {
    'nop': nop,
    'acc': acc,
    'jmp': jmp
}

def exec(ctx, cmds):
    while True:
        ip = ctx['ip']
        if ip >= len(cmds):
            return ctx['acc'], ctx['trace'], True
        if cmds[ip]['used']:
            return ctx['acc'], ctx['trace'], False
        code[cmds[ip]['cmd']](ctx, cmds[ip]['op'])
        cmds[ip]['used'] = True

def run(cmds):
    ctx = {'ip': 0, 'acc': 0, 'trace': []}
    return exec(ctx, cmds)

def morphe(cmds, ip):
    newcmds = deepcopy(cmds)
    if newcmds[ip]['cmd'] == 'nop':
        newcmds[ip]['cmd'] = 'jmp'
    elif newcmds[ip]['cmd'] == 'jmp':
        newcmds[ip]['cmd'] = 'nop'
    else:
        raise Exception('morphing invalid command')
    return newcmds

def fix_bug(cmds, trace):
    for bugip in trace:
        ncmds = morphe(cmds, bugip)
        acc, _, works = run(ncmds)
        if works:
            #print(f'Found! fix cmd idx {bugip}')
            return acc

cmds = get_cmds()

p1, trace, _ = run(deepcopy(cmds))
p2 = fix_bug(cmds, reversed(trace))

print(f'Part1: acc {p1}')
print(f'Part2: acc {p2}')
