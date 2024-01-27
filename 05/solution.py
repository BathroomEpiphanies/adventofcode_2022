from __future__ import annotations

import collections
import copy
import itertools
import re


def parse_input(file_handle):
    stacks = []
    lines = (l.rstrip() for l in file_handle.readlines())
    for line in lines:
        if not line:
            break
        stacks.append(line)
    stacks = [''.join(l).strip() for l in list(itertools.zip_longest(*stacks[:-1], fillvalue=' '))[1::4]]
    stacks = [collections.deque(reversed(s)) for s in stacks]
    moves = [[int(a),int(b)-1,int(c)-1] for a,b,c in (m.groups() for m in (re.match(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', l) for l in lines))]
    return stacks,moves


def part1(problem_input):
    stacks,moves = problem_input
    stacks = copy.deepcopy(stacks)
    for a,b,c in moves:
        for _ in range(a):
            stacks[c].append(stacks[b].pop())
        #[print(s) for s in stacks]
        #print()
    return ''.join([s.pop() for s in stacks])


def part2(problem_input):
    stacks,moves = problem_input
    stacks = copy.deepcopy(stacks)
    tmp = collections.deque()
    for a,b,c in moves:
        for _ in range(a):
            tmp.append(stacks[b].pop())
        for _ in range(a):
            stacks[c].append(tmp.pop())
        #[print(s) for s in stacks]
        #print()
    return ''.join([s.pop() for s in stacks])
