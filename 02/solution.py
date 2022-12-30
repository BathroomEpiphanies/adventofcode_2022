import sys


def parse_input(file_handle):
    return [l.strip().split(' ') for l in file_handle.readlines()]


def star1(problem_input):
    score = {
        'A': {'X': 1+3, 'Y':2+6, 'Z':3+0},
        'B': {'X': 1+0, 'Y':2+3, 'Z':3+6},
        'C': {'X': 1+6, 'Y':2+0, 'Z':3+3},
    }
    return sum(score[a][b] for a,b in problem_input)


def star2(problem_input):
    score = {
        'A': {'X': 3+0, 'Y':1+3, 'Z':2+6},
        'B': {'X': 1+0, 'Y':2+3, 'Z':3+6},
        'C': {'X': 2+0, 'Y':3+3, 'Z':1+6},
    }
    return sum(score[a][b] for a,b in problem_input)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
