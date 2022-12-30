import sys


def parse_input(file_handle):
    return [int(l) for l in file_handle.readlines()]


def star(problem_input, key=1, rounds=1):
    original = [[p,v*key] for p,v in enumerate(problem_input)]
    crypto = [o for o in original]
    for _ in range(rounds):
        for o in original:
            p,v = o
            t = (p+v)%(len(original)-1)
            if p<=t:
                for j in range(p+1,t+1):
                    crypto[j][0] -= 1
            else:
                for j in range(t,p):
                    crypto[j][0] += 1
            o[0] = t
            crypto.sort(key=lambda x: x[0])
    crypto = [v for p,v in crypto]
    i = crypto.index(0)
    coordinates = [crypto[(i+d)%len(original)] for d in [1000,2000,3000]]
    return sum(coordinates)


def star1(problem_input):
    return star(problem_input)


def star2(problem_input):
    return star(problem_input, key=811589153, rounds=10)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
