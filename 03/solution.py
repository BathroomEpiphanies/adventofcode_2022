import more_itertools
import string
import sys


def parse_input(file_handle):
    return [l.strip() for l in file_handle.readlines()]


priorities = {a:i for i,a in enumerate(string.ascii_lowercase+string.ascii_uppercase, 1)}


def star1(problem_input):
    #return sum(priorities[next(iter(set(line[:len(line)//2]) & set(line[len(line)//2:])))] for line in problem_input)
    total = 0
    for line in problem_input:
        intersection = set(line[:len(line)//2]) & set(line[len(line)//2:])
        total += priorities[list(intersection)[0]]
    return total


def star2(problem_input):
    total = 0
    for l1,l2,l3 in more_itertools.grouper(3, problem_input):
        intersection = set(l1) & set(l2) & set(l3)
        total += priorities[list(intersection)[0]]
    return total


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
