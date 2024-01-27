from __future__ import annotations

import collections
import functools


gusts = {
    '>': +1+0j,
    '^': +0-1j,
    '<': -1+0j,
    'v': +0+1j,
    '#': +0+0j,
}


def parse_input(file_handle):
    valley = {c+r*1j:[w] for r,row in enumerate((l.strip() for l in file_handle.readlines()), -1) for c,w in enumerate(row, -1) if w in gusts}
    maxr,maxc = round(max(v.imag for v in valley)),round(max(v.real for v in valley))
    valley[(maxc-1)+(maxr+1)*1j] = ['#']
    valley[(    +0)+(    -2)*1j] = ['#']
    valley['maxr'] = maxr
    valley['maxc'] = maxc
    return valley


def advance_valley(valley):
    result = collections.defaultdict(list)
    for p,d in valley.items():
        if not isinstance(d, list):
            continue
        for w in d:
            q = p+gusts[w]
            if w!='#':
                q = round(q.real)%(valley['maxc']) + round(q.imag)%(valley['maxr'])*1j
            result[q].append(w)
    result['maxr'] = valley['maxr']
    result['maxc'] = valley['maxc']
    return result


def print_valley(valley, expedition, goal):
    result = [['.']*(valley['maxc']+2) for _ in range(valley['maxr']+4)]
    for p,d in valley.items():
        if p in ['maxr','maxc']:
            continue
        result[round(p.imag+2)][round(p.real+1)] = d[0] if len(d)==1 else str(len(d))
    result[round(expedition.imag+2)][round(expedition.real+1)] = 'E'
    result[round(goal.imag+2)][round(goal.real+1)] = 'G'
    print('\n'.join(''.join(r) for r in result[1:-1]))


def star(valley, trips=1):
    @functools.cache
    def get_valley(time):
        if time==0:
            return valley
        else:
            return advance_valley(get_valley(time-1))

    time,start,goal = 0, 0-1j, (valley['maxc']-1)+(valley['maxr'])*1j
    # print_valley(valley, start, goal)
    for _ in range(trips):
        visited = set()
        queue = collections.deque()
        queue.appendleft((time,start))
        while queue:
            time,pos = item = queue.pop()
            if item in visited:
                continue
            visited.add(item)
            dest_valley = get_valley(time+1)
            if pos==goal:
                break
            for d in [+1+0j, +0-1j, -1+0j, +0+1j, +0+0j]:
                if pos+d not in dest_valley:
                    queue.appendleft((time+1,pos+d))
        time,start,goal = time,goal,start
    return time


def part1(problem_input):
    return star(problem_input)


def part2(problem_input):
    return star(problem_input, trips=3)
