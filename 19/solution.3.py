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

    def __mul__(self, other):
        return atuple(a*b for a,b in zip(self, other))


def parse_input(file_handle):
    blueprints = []
    for line in (l.strip() for l in sys.stdin.readlines()):
        m = re.match(r'Blueprint [0-9]+: Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.', line)
        n = [int(a) for a in m.groups()]
        #print(m)
        blueprints.append((
            (atuple((1,0,0,0)), atuple((n[0],    0,    0,    0))),
            (atuple((0,1,0,0)), atuple((n[1],    0,    0,    0))),
            (atuple((0,0,1,0)), atuple((n[2], n[3],    0,    0))),
            (atuple((0,0,0,1)), atuple((n[4],    0, n[5],    0))),
            (atuple((0,0,0,0)), atuple((   0,    0,    0,    0))),
        ))
        
    return blueprints


def star(blueprints, maxtime):
    for blueprint in blueprints[:1]:
        maxcosts = [max(r) for r in zip(*(c for r,c in blueprint))][:3]
        #print(maxcosts)
        #exit()
        q = queue.PriorityQueue()
        q.put((
            None,
            0,
            atuple((1,0,0,0)),
            atuple((1,0,0,0))
        ))
        best = 0
        h = [0]*maxtime
        while not q.empty():
            w,time,robots,resources = q.get()
            #print(w,time,robots,resources)
            if time==maxtime-1:
                total = resources[3]+robots[3]
                if total>best:
                    best = total
                    print(best, time+1)
                continue
            if resources[3]<h[time]:
                continue
            else:
                h[time] = resources[3]
            for robot,cost in blueprint:
                if cost<=resources and robots+robot<maxcosts:
                    #w = resources+robots-cost
                    #w = atuple( (-w[3],-w[2],-w[1],-w[0]) )
                    w = robots+robot
                    w = (time, -w[3],-w[2],-w[1],-w[0])
                    q.put((
                        w,
                        time+1,
                        robots+robot,
                        resources+robots-cost
                    ))
            
        

def part1(problem_input):
    return star(problem_input, 20)


if __name__=='__main__':
    import sys
    problem_input = parse_input(sys.stdin)
    print(f'*1: {part1(problem_input)}')
    #print(f'*2: {part2(problem_input)}')
