import collections
import dataclasses
import math
import sys
import typing


@dataclasses.dataclass
class Monkey:
    items: collections.deque = collections.deque()
    modulus: int = 0
    operation: typing.Callable = lambda x: x
    toss: typing.Callable = lambda x: None
    inspections: int = 0


def parse_input(file_handle):
    monkeys = []
    lines = (l.strip() for l in file_handle.readlines())
    try:
        while True:
            line = next(lines)
            number = int(line.split(' ')[1][:-1])
            line = next(lines)
            items = collections.deque([int(n) for n in line.split(': ')[1].split(',')])
            line = next(lines)
            operation = eval(f'lambda old: {line.split("= ")[1]}')
            line = next(lines)
            modulus = int(line.split('by ')[1])
            line = next(lines)
            true = int(line.split('monkey ')[1])
            line = next(lines)
            false = int(line.split('monkey ')[1])
            toss = eval(f'lambda worry: {true} if worry%{modulus}==0 else {false}')
            monkeys.append(Monkey(items=items, modulus=modulus, operation=operation, toss=toss))
            line = next(lines)
    except StopIteration:
        pass
    return monkeys


def star(monkeys, rounds, divisor):
    lcm = math.lcm(*(m.modulus for m in monkeys))
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspections += 1
                worry = monkey.items.popleft()
                worry = monkey.operation(worry)%lcm//divisor
                monkeys[monkey.toss(worry)].items.append(worry)
    inspections = sorted((m.inspections for m in monkeys), reverse=True)
    return inspections[0]*inspections[1]


def star1(monkeys):
    return star(monkeys, rounds=20, divisor=3)


def star2(monkeys):
    return star(monkeys, rounds=10000, divisor=1)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
