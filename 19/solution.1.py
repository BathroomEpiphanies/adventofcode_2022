import functools
import numpy as np
import queue
import re
import sys


class atuple(tuple):

    def __new__ (cls, tuple_):
        return super(atuple, cls).__new__(cls, tuple_)
    
    def __str__(self):
        return super().__str__()
    
    def __hash__(self):
        return super().__hash__()
    
    def __eq__(self, other):
        return super().__eq__(other)
    
    def __lt__(self, other):
        return all(a<b for a,b in zip(self, other))
    
    def __gt__(self, other):
        return all(a>b for a,b in zip(self, other))
    
    def __le__(self, other):
        return all(a<=b for a,b in zip(self, other))
    
    def __ge__(self, other):
        return all(a>=b for a,b in zip(self, other))
    
    def __add__(self, other):
        return atuple(a+b for a,b in zip(self, other))
    
    def __sub__(self, other):
        return atuple(a-b for a,b in zip(self, other))


def parse_input(file_handle):
    blueprints = []
    for line in (l.strip() for l in sys.stdin.readlines()):
        m = re.match(r'Blueprint [0-9]+: Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.', line).groups()
        #print(m)
        blueprints.append((
            (
                (atuple((0,0,0,1)), atuple( (int(m[4]),        0,   int(m[5]),     0) )),
                (atuple((0,0,1,0)), atuple( (int(m[2]),  int(m[3]),       0,       0) )),
                (atuple((0,1,0,0)), atuple( (int(m[1]),        0,         0,       0) )),
                (atuple((1,0,0,0)), atuple( (int(m[0]),        0,         0,       0) )),
                (atuple((0,0,0,0)), atuple( (      0,          0,         0,       0) )),
            )
        ))
    return blueprints


#def part1(blueprints):
#    for number,blueprint in enumerate(blueprints, 1):
#        costs,robots,resources = blueprint
#        print(costs,robots,resources)
#        @functools.cache
#        def search(depth, robots, resources, building):
#            print('  '*depth, depth, robots, resources, building)
#            if depth>24:
#                return resources[3]
#            if not resources<atuple((50,50,50,50)):
#                return 0
#            else:
#                resources += robots
#                robots += building
#                options = []
#                for building,cost in costs:
#                    #print(resources,cost)
#                    if cost<=resources:
#                        options.append(search(depth+1, robots, resources-cost, building))
#                return max(options)
#        print(search(0, robots, resources, atuple((0,0,0,0))) )
#        return None


#def part1(blueprints):
#    quality = 0
#    for number,blueprint in enumerate(blueprints, 1):
#        print(blueprint)
#        cache = {}
#        def search(time, robots, resources, building):
#            if time==0:
#                return 0
#            else:
#                resources += robots
#                robots += building
#                key = (time,tuple(robots[0:2]),tuple(resources[0:2]))
#                if key in cache:
#                    return cache[key]+time*building[3]
#                options = []
#                for build,cost in blueprint:
#                    if cost<=resources:
#                        options.append(search(time-1, atuple((robots[0],robots[1],robots[2],0)), resources-cost, build))
#                best = max(options)
#                cache[key] = best
#                return best+time*building[3]
#        top = search(24, atuple((1,0,0,0)), atuple((0,0,0,0)), atuple((0,0,0,0)))
#        print(number, top)
#        quality += number*top
#    return quality


def part1(blueprints):
    blueprint = blueprints[0]
    def search():
        return

    print(search(time, atuple((1,0,0,0)), atuple((0,0,0,0))))

        
def part2(problem_input):
    return None


if __name__=='__main__':
    import sys
    problem_input = parse_input(sys.stdin)
    print(f'*1: {part1(problem_input)}')
    print(f'*2: {part2(problem_input)}')
