from __future__ import annotations

import more_itertools


def parse_input(file_handle):
    return file_handle.readline().strip()


def find_marker(message, marker_length):
    for position,window in enumerate(more_itertools.windowed(message, marker_length), marker_length):
        if len(set(window))==marker_length:
            return position
    raise Exception(f'marker of length {marker_length} not found')


def part1(problem_input):
    return find_marker(problem_input, 4)


def part2(problem_input):
    return find_marker(problem_input, 14)
