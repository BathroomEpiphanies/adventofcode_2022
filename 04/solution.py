import more_itertools
import re
import string
import sys


def parse_input(file_handle):
    return [((a,b),(c,d)) for a,b,c,d in ([int(n) for n in m.groups()] for m in (re.match(r'([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)', l) for l in file_handle.readlines()))]


def star1(problem_input):
    count = 0
    for ((a,b),(c,d)) in problem_input:
        if a<=c and d<=b or c<=a and b<=d:
            count += 1
    return count


def star2(problem_input):
    count = 0
    for ((a,b),(c,d)) in problem_input:
        if a<=c and c<=b or c<=a and a<=d:
            count += 1
    return count


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
