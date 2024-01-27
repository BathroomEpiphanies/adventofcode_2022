from __future__ import annotations

import math


def parse_input(file_handle):
    return [l.strip() for l in file_handle.readlines()]


values = {
    '2':  2,
    '1':  1,
    '0':  0,
    '-': -1,
    '=': -2,
}
values.update({d:k for k,d in values.items()})


def to_snafu(decimal):
    decimal += sum(2*pow(5,i) for i in range(math.ceil(math.log(decimal,5))))
    result = []
    for i in range(math.ceil(math.log(decimal,5))):
        result.append(values[decimal%5-2])
        decimal //= 5
    return ''.join(reversed(result))


def part1(snafus):
    return to_snafu(sum(sum(values[d]*pow(5,i) for i,d in enumerate(reversed(snafu))) for snafu in snafus))
