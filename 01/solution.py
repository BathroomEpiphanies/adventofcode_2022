from __future__ import annotations


def parse_input(file_handle):
    test_input = [[]]
    for line in (l.strip() for l in file_handle.readlines()):
        if not line:
            test_input.append([])
        else:
            test_input[-1].append(int(line))
    return test_input


def part1(problem_input):
    most = 0
    for elf in problem_input:
        most = max(most, sum(elf))
    return most


def part2(problem_input):
    elves = [sum(elf) for elf in problem_input]
    elves.sort()
    return sum(elves[-3:])
