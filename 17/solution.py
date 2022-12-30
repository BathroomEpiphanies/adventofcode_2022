import itertools
import sys
    

def parse_input(file_handle):
    return [-1 if c=='<' else +1 for c in file_handle.readline().strip()]


pieces = [
    # @@@@
    {p+2 for p in {0+0j,1+0j,2+0j,3+0j}},
    #  @
    # @@@
    #  @
    {p+2 for p in {1+0j,0+1j,1+1j,2+1j,1+2j}},
    #   @
    #   @
    # @@@
    {p+2 for p in {0+0j,1+0j,2+0j,2+1j,2+2j}},
    # @
    # @
    # @
    # @
    {p+2 for p in {0+0j,0+1j,0+2j,0+3j}},
    # @@
    # @@
    {p+2 for p in {0+0j,1+0j,0+1j,1+1j}},
]


def print_stack(stack, piece=set()):
    height = round(max(s.imag for s in piece)) if piece else round(max(s.imag for s in stack))
    for row in range(height,0,-1):
        print('|'+''.join('#' if col+row*1j in stack else '@' if col+row*1j in piece else '.' for col in range(7))+'|')
    print('+-------+')
    return
              

def star(problem_input, total_turns):
    moves = (m for m in itertools.chain.from_iterable(itertools.repeat(problem_input)))
    stack = {0+0j,1+0j,2+0j,3+0j,4+0j,5+0j,6+0j}
    height = 0
    increases = []
    for turn in range(total_turns):
        new_height = round(max(s.imag for s in stack))
        increases.append(new_height-height)
        height = new_height
        piece = {p+(height+4)*1j for p in pieces[turn%len(pieces)]}
        for move in moves:
            tmp = {p+move for p in piece}
            piece = piece if stack&tmp or any(p.real<0 or p.real>6 for p in tmp) else tmp
            tmp = {p-1j for p in piece}
            if stack&tmp:
                stack |= piece
                break
            else:
                piece = tmp
        for i in range(10,len(increases)//2,len(pieces)):
            if tuple(increases[-i:]) == tuple(increases[-2*i:-i]):
                return \
                    height + \
                    (total_turns-turn)//i*sum(increases[-i:]) + \
                    sum(increases[-i:-i+(total_turns-turn)%i])
    return round(max(s.imag for s in stack))


def star1(problem_input):
    return star(problem_input, 2_022)


def star2(problem_input):
    return star(problem_input, 1_000_000_000_000)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
