import collections
import re
import sys
    

def parse_input(file_handle):
    lines = [l.strip() for l in file_handle.readlines()]
    sensors = [
        ((int(a),int(b),abs(int(x)-int(a))+abs(int(y)-int(b))),(int(x),int(y))) for a,b,x,y in
        (
            m.groups() for m in (
                re.match(r'Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)', line)
                for line in lines
            )
            if m
        )
    ]
    sensors.sort()
    m = re.match(r'row=([-0-9]+), dimension=([0-9]+)', lines[-1])
    if m:
        return sensors,int(m.groups()[0]),int(m.groups()[1])
    else:
        return sensors,2_000_000,4_000_000


class MultiInterval:
    def __init__(self):
        self.intervals = []
        return
    
    def __add__(self, other):
        x,y = other
        tmp = []
        for a,b in self.intervals:
            if y<a-1 or x>b+1:
                tmp.append((a,b))
            else:
                x,y = min(x,a),max(y,b)
        tmp.append((x,y))
        tmp.sort()
        self.intervals = tmp
        return self
    
    def __sub__(self, other):
        x,y = other
        tmp = []
        for a,b in self.intervals:
            if y<a or x>b:
                tmp.append((a,b))
            else:
                if a<x:
                    tmp.append((a,x-1))
                if y<b:
                    tmp.append((y+1,b))
        tmp.sort()
        self.intervals = tmp
        return self
    
    def __len__(self):
        return sum(b-a+1 for a,b in self.intervals)
    
    def __str__(self):
        return ','.join(str(i) for i in self.intervals)


def coverage(sensors,row):
    tmp = MultiInterval()
    for (a,b,d),(x,y) in sensors:
        e = d-abs(row-b)
        if e>=0:
            tmp += (a-e,a+e)
    return tmp
    

def star1(problem_input):
    sensors,row,_ = problem_input
    row_coverage = coverage(sensors, row)
    for (_,_,_),(x,y) in sensors:
        if y==row:
            row_coverage = row_coverage-(x,x)
    print('row_coverage',row_coverage)
    return len(row_coverage)


def star2(problem_input):
    sensors,row,dimension = problem_input
    for row in range(dimension):
        row_coverage = coverage(sensors, row)
        #print(row, row_coverage)
        if len(row_coverage.intervals)>1:
            answer = row+4_000_000*(row_coverage.intervals[0][1]+1)
            print(row_coverage)
            print(answer)
    return answer


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
