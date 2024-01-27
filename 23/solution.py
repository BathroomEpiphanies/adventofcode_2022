from __future__ import annotations

import collections
import itertools


def parse_input(file_handle):
    return {c+r*1j for r,line in enumerate(l.strip() for l in file_handle.readlines()) for c,s in enumerate(line) if s=='#'}


def star(elves, maxturns=None):
    elves = elves.copy()
    move_directions = collections.deque([
        (+0-1j, [-1-1j, +0-1j, +1-1j]),
        (+0+1j, [-1+1j, +0+1j, +1+1j]),
        (-1+0j, [-1-1j, -1+0j, -1+1j]),
        (+1+0j, [+1-1j, +1+0j, +1+1j]),
    ])
    all_directions = {c for _,checks in move_directions for c in checks}
    for turn in range(1,maxturns+1) if maxturns is not None else itertools.count(1):
        propositions = collections.defaultdict(list)
        for elf in elves:
            if all(elf+d not in elves for d in all_directions):
                continue
            for move,checks in move_directions:
                if any(elf+c in elves for c in checks):
                    continue
                propositions[elf+move].append(elf)
                break
        if not propositions:
            break
        for proposition,proposers in propositions.items():
            if len(proposers)>1:
                continue
            elves.remove(proposers[0])
            elves.add(proposition)
        move_directions.rotate(-1)
        
    bx,ax = max(e.real for e in elves),min(e.real for e in elves)
    by,ay = max(e.imag for e in elves),min(e.imag for e in elves)
    return turn,round((bx-ax+1)*(by-ay+1)-len(elves))


def part1(problem_input):
    return star(problem_input, maxturns=10)[1]

def part2(problem_input):
    return star(problem_input)[0]
