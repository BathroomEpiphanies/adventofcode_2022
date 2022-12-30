import more_itertools
import sys


def parse_input(file_handle):
    return file_handle.readline().strip()


def find_marker(message, marker_length):
    for position,window in enumerate(more_itertools.windowed(message, marker_length), marker_length):
        if len(set(window))==marker_length:
            return position
    raise Exception(f'marker of length {marker_length} not found')


def star1(problem_input):
    return find_marker(problem_input, 4)


def star2(problem_input):
    return find_marker(problem_input, 14)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
