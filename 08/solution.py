import numpy as np
import sys


def parse_input(file_handle):
    return np.array([[int(n) for n in l.strip()] for l in file_handle.readlines()])


def star1(problem_input):
    def visible_left_to_right(trees):
        max_heights = np.pad(np.maximum.accumulate(trees, axis=1), pad_width=1, mode='constant', constant_values=-1)
        return trees > max_heights[1:-1,:-2]
    
    visible = np.any(
        (visible_left_to_right(problem_input),
         np.flip(visible_left_to_right(np.flip(problem_input, axis=1)), axis=1),
         visible_left_to_right(problem_input.T).T,
         np.flip(visible_left_to_right(np.flip(problem_input.T, axis=1)), axis=1).T),
        axis = 0
    )
    
    return np.sum(visible)


def star2(problem_input):
    visible = np.zeros_like(problem_input)
    for r,row in enumerate(problem_input):
        for c,tree in enumerate(row):
            prod = 1
            total = 0
            for cp in range(c+1,len(row)):
                total += 1
                if problem_input[r][cp]>=problem_input[r][c]:
                    break
            prod *= total
            total = 0
            for cp in range(c-1,-1,-1):
                total += 1
                if problem_input[r][cp]>=problem_input[r][c]:
                    break
            prod *= total
            total = 0
            for rp in range(r+1,len(problem_input)):
                total += 1
                if problem_input[rp][c]>=problem_input[r][c]:
                    break
            prod *= total
            total = 0
            for rp in range(r-1,-1,-1):
                total += 1
                if problem_input[rp][c]>=problem_input[r][c]:
                    break
            prod *= total
            visible[r][c] = prod
    return np.max(visible)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
