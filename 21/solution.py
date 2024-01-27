from __future__ import annotations

import operator
import re
import z3


def parse_input(file_handle):
    tree = {}
    for line in file_handle.readlines():
        m = re.match(r'([a-z]+)\: ([a-z]+) (.) ([a-z]+)', line)
        n = re.match(r'([a-z]+)\: ([-0-9]+)', line)
        if m:
            g = m.groups()
            tree[g[0]] = [g[1],g[2],g[3]]
        if n:
            g = n.groups()
            tree[g[0]] = int(g[1])
    return tree


operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}


def part1(tree):
    solver = z3.Solver()
    variables = {}
    for variable in tree:
        variables[variable] = z3.Real(variable)
    for variable,expression in tree.items():
        if isinstance(expression, int):
            solver.add(variables[variable] == expression)
        else:
            solver.add(variables[variable] == operators[expression[1]](variables[expression[0]], variables[expression[2]]))
    solver.check()
    model = solver.model()
    return model[variables['root']].as_long()


def part2(tree):
    solver = z3.Solver()
    variables = {'humn':z3.Real('humn')}
    for variable in tree:
        variables[variable] = z3.Real(variable)
    solver.add(variables[tree['root'][0]]==variables[tree['root'][2]])
    for variable,expression in ((v,e) for v,e in tree.items() if v not in ['humn','root']):
        if isinstance(expression, int):
            solver.add(variables[variable] == expression)
        else:
            solver.add(variables[variable] == operators[expression[1]](variables[expression[0]], variables[expression[2]]))
    solver.check()
    model = solver.model()
    return model[variables['humn']].as_long()
