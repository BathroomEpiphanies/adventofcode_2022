import collections
import numpy as np
import sys


def parse_input(file_handle):
    return set([Point3D(l.strip().split(',')) for l in file_handle.readlines()])


class Point3D:
    
    def __init__(self, point):
        self.point = tuple((int(n) for n in point))
        return
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Point3D((-a for a in self.point))
    
    def __add__(self, other):
        return Point3D((a+b for a,b in zip(self.point, other.point)))

    def __add__(self, other):
        return Point3D((a+b for a,b in zip(self.point, other.point)))

    def __sub__(self, other):
        return Point3D((a-b for a,b in zip(self.point, other.point)))
    
    def __eq__(self, other):
        return self.point==other.point
    
    def __hash__(self):
        return hash(self.point)
    
    def __str__(self):
        return str(self.point)
    
    def neighbours(self):
        __neighbours6 = [Point3D(n) for n in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]]
        return [self+n for n in __neighbours6]

    def in_volume(self, p1, p2):
        return all(a>=b for a,b in zip(self.point,p1.point)) and all(a<=b for a,b in zip(self.point,p2.point))


def star1(points):
    return sum(6-sum(n in points for n in point.neighbours()) for point in points)


def star2(points):
    p1 = -Point3D((1,1,1))+Point3D((min(p.point[0] for p in points),min(p.point[1] for p in points),min(p.point[2] for p in points)))
    p2 = +Point3D((1,1,1))+Point3D((max(p.point[0] for p in points),max(p.point[1] for p in points),max(p.point[2] for p in points)))
    area = 0
    queue = collections.deque([p1])
    found = set([p1])
    while queue:
        p = queue.pop()
        for n in p.neighbours():
            if n in points:
                area += 1
            elif n not in found and n.in_volume(p1,p2):
                queue.append(n)
                found.add(n)
    return area


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
