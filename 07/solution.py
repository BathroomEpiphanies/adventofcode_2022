import sys


class node:
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        self.files = {}
        self.children = {}
        self.indent = parent.indent+2 if parent else 0
        self.size = None
    
    def __str__(self):
        result  = f'{" "*self.indent}{self.name}\n'
        for name,size in self.files.items():
            result += f'{" "*self.indent}{name}: {size}\n'
        for name,child in self.children.items():
            #result += f'{name}\n{child}\n'
            result += f'{child}'
        result += f'{" "*self.indent}size = {self.size}\n'
        return result


def parse_input(file_handle):
    def calc_size_recursive(pwd):
        pwd.size = sum(s for _,s in pwd.files.items())
        for _,child in pwd.children.items():
            pwd.size += calc_size_recursive(child)
        return pwd.size
    
    lines = [l.strip() for l in file_handle.readlines()]
    root = node(None, '/')
    pwd = root
    for line in lines[1:]:
        if line == '$ ls':
            continue
        elif line == '$ cd ..':
            pwd = pwd.parent
        elif line[:4] == '$ cd':
            pwd = pwd.children[line[5:]]
        elif line[:4] == 'dir ':
            pwd.children[line[4:]] = node(pwd, line[4:])
        else:
            size,name = line.split(' ')
            pwd.files[name] = int(size)
    calc_size_recursive(root)
    print(root, file=sys.stderr)
    return root


def star1(problem_input):
    def sum_selected(pwd, total=0):
        if pwd.size<100000:
            total += pwd.size
        for _,child in pwd.children.items():
            total = sum_selected(child, total)
        return total
    total = sum_selected(problem_input)
    return total


def star2(problem_input):
    needed_space = 30_000_000-(70_000_000-problem_input.size)
    def find_smallest(pwd, best=float('inf')):
        for _,child in pwd.children.items():
            best = find_smallest(child, best)
        if pwd.size>needed_space and pwd.size<best:
            return pwd.size
        else:
            return best
    return find_smallest(problem_input)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
