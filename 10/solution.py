import collections
import sys

import aoc_display


def parse_input(file_handle):
    problem_input = []
    for line in (l.strip() for l in file_handle.readlines()):
        l = line.split(' ')
        problem_input.append((l[0],None) if len(l)==1 else (l[0],int(l[1])))
    return problem_input


def star1(problem_input):
    values = [1]
    for instruction,value in problem_input:
        if instruction=='noop':
            values.append(values[-1])
        elif instruction=='addx':
            values.append(values[-1])
            values.append(values[-1]+value)
    total = 0
    for t in range(20,len(values),40):
        total += t*values[t-1]
    return total


def star2(problem_input):
    display = []
    sprite = 0
    time = 0
    for instruction,value in problem_input:
        if instruction=='noop':
            display.append('#' if sprite<=time%40<sprite+3 else '.')
            time += 1
        elif instruction=='addx':
            display.append('#' if sprite<=time%40<sprite+3 else '.') 
            time += 1
            display.append('#' if sprite<=time%40<sprite+3 else '.') 
            time += 1
            sprite += value
    try:
        formatted = [display[t:t+40] for t in range(0,len(display),40)]
        return aoc_display.decode(formatted)
    except KeyError:
        return '\n'+'\n'.join(''.join(display[t:t+40]) for t in range(0,len(display),40))


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
