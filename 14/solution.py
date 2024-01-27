from __future__ import annotations

import copy
import itertools


def print_rock(rocks):
    minx,maxx = int(min(r.real for r in rocks)),int(max(r.real for r in rocks))
    miny,maxy = int(min(r.imag for r in rocks)),int(max(r.imag for r in rocks))
    tmp = [['.']*(maxx-minx+3) for _ in range(maxy-miny+3)]
    for p,r in rocks.items():
        tmp[int(p.imag-miny+1)][int(p.real-minx+1)] = r
    [print(''.join(t)) for t in tmp]


def parse_input(file_handle):
    formations = [[int(a)+int(b)*1j for a,b in [c.split(',') for c in line.strip().split(' -> ')]] for line in file_handle.readlines()]
    rocks = {500+0j:'+'}
    for formation in formations:
        for p1,p2 in zip(formation[:-1], formation[1:]):
            l = int(abs(p2-p1))
            d = (p2-p1)/l
            for i in range(l+1):
                p = p1+i*d
                rocks[p] = '#'
    bottom = int(max(r.imag for r in rocks))
    return rocks,bottom


def star(problem_input, has_floor=False):
    rocks,bottom = problem_input
    rocks = copy.deepcopy(rocks)
    for i in itertools.count():
        #print_rock(rocks)
        sand = 500+0j
        while has_floor and rocks[500+0j]=='+' or not has_floor and sand.imag<bottom:
            if sand.imag>=bottom+1:
                rocks[sand] = 'o'
                break
            elif sand+1j not in rocks:
                sand += 0+1j
            elif sand-1+1j not in rocks:
                sand += -1+1j
            elif sand+1+1j not in rocks:
                sand += 1+1j
            else:
                rocks[sand] = 'o'
                break
        else:
            break
    return i


def part1(problem_input):
    return star(problem_input)


def part2(problem_input):
    return star(problem_input, has_floor=True)
