import collections
import sys


def parse_input(file_handle):
    return [(a,int(b)) for a,b in (l.strip().split(' ') for l in file_handle.readlines())]


dirs = {
    "R":  1+0j,
    "U":  0+1j,
    "L": -1+0j,
    "D":  0-1j,
}


pull = collections.defaultdict(lambda: 0, {
    -2+2j:-1+1j,  -1+2j:-1+1j,   0+2j: 0+1j,   1+2j: 1+1j,   2+2j: 1+1j,
    -2+1j:-1+1j,                                             2+1j: 1+1j,
    -2+0j:-1+0j,                                             2+0j: 1+0j,
    -2-1j:-1-1j,                                             2-1j: 1-1j,
    -2-2j:-1-1j,  -1-2j:-1-1j,   0-2j: 0-1j,   1-2j: 1-1j,   2-2j: 1-1j,
})


def star1(problem_input):
    head,tail = 0+0j,0+0j
    visited = collections.defaultdict(lambda: False,  {tail:True})
    for d,l in problem_input:
        for _ in range(l):
            head += dirs[d]
            tail += pull[head-tail]
            visited[tail] = True
    return len(visited)


def star2(problem_input):
    knots = [0+0j]*10
    visited = collections.defaultdict(lambda: False,  {knots[9]:True})
    for d,l in problem_input:
        for _ in range(l):
            knots[0] += dirs[d]
            for k in range(9):
                knots[k+1] += pull[knots[k]-knots[k+1]]
            visited[knots[9]] = True
    return len(visited)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
