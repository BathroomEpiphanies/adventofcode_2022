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
        return any(a<b for a,b in zip(self, other))
    
    def __gt__(self, other):
        return any(a>b for a,b in zip(self, other))
    
    def __le__(self, other):
        return all(a<=b for a,b in zip(self, other))
    
    def __ge__(self, other):
        return all(a>=b for a,b in zip(self, other))
    
    def __add__(self, other):
        return atuple(a+b for a,b in zip(self, other))
    
    def __sub__(self, other):
        return atuple(a-b for a,b in zip(self, other))

    def __mul__(self, other):
        return atuple(a*b for a,b in zip(self, other))


def parse_input(file_handle):
    blueprints = []
    for line in (l.strip() for l in sys.stdin.readlines()):
        m = re.match(r'Blueprint [0-9]+: Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.', line)
        n = [int(a) for a in m.groups()]
        #print(m)
        blueprints.append((
            (atuple((1,0,0,0)), atuple((n[0],    0,    0))),
            (atuple((0,1,0,0)), atuple((n[1],    0,    0))),
            (atuple((0,0,1,0)), atuple((n[2], n[3],    0))),
            (atuple((0,0,0,1)), atuple((n[4],    0, n[5]))),
            #(atuple((0,0,0,0)), atuple((   0,    0,    0))),
        ))
        
    return blueprints


def part1(blueprints):
    total = 0
    for number,blueprint in enumerate(blueprints, 1):
        print(blueprint)
        [print(l) for l in zip(*(c for r,c in blueprint))]
        maxcosts = atuple((*(max(l) for l in zip(*(c for r,c in blueprint))), 1000))
        print(maxcosts)
        #@functools.cache
        def search(time, robots, resources):
            #print('  '*(24-time), time, robots, resources)
            if time==1:
                return 0
            else:
                options = []
                for robot,cost in blueprint:
                    #print(robot,cost,robot*robots,robot*maxcosts,robot*maxcosts>robot*robots, cost<=resources)
                    if cost<=resources and robot*robots<robot*maxcosts:
                        options.append(search(time-1, robots+robot, resources-cost+robots) + (time-2 if robot[3] else 0))
                options.append(search(time-1, robots, resources+robots))
                return max(options)
        quality = search(time=24, robots=atuple((1,0,0)), resources=atuple((1,0,0)))
        print(number, quality)
        total += number*quality
    return total

        
def part2(blueprints):
    total = 1
    for number,blueprint in enumerate(blueprints[0:3], 1):
        print(blueprint)
        @functools.cache
        def search(time, robots, resources):
            #print('  '*(24-time), time, robots, resources)
            #if time==2:
            #    return 1 if blueprint[0][1]<=resources else 0
            if time==1:
                return 0
            else:
                return max(
                    search(time-1, robots+robot, resources-cost+robots) + (time-2 if robot[3] else 0)
                    for robot,cost in blueprint if cost<=resources
                )
        quality = search(time=32, robots=atuple((1,0,0)), resources=atuple((1,0,0)))
        print(number, quality)
        total *= quality
    return total


if __name__=='__main__':
    import sys
    problem_input = parse_input(sys.stdin)
    print(f'*1: {part1(problem_input)}')
    #print(f'*2: {part2(problem_input)}')
