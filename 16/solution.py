import networkx
import collections
import itertools
import pprint
import re
import sys
    

def parse_input(file_handle):
    cave = networkx.Graph()
    for line in file_handle.readlines():
        valve,rate,tunnels = re.match(r'Valve ([A-Z]+) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)' ,line).groups()
        tunnels = tunnels.split(', ')
        cave.add_node(valve, rate=int(rate))
        for tunnel in tunnels:
            cave.add_edge(valve, tunnel)
    direct_distances = {a:b for a,b in networkx.all_pairs_shortest_path_length(cave)}
    direct_distances[None] = {}
    for a in list(direct_distances):
        direct_distances[None][a] = 100
        direct_distances[a][None] = 0
    #pprint.pprint(direct_distances)
    remaining = {v:d['rate'] for v,d in cave.nodes(data=True) if d['rate']>0}
    return direct_distances,remaining


def star1(problem_input):
    def search(distances, time, position, valves):
        flow = valves[position]*(time-1)
        maxadd = 0
        valves = {v:r for v,r in valves.items() if v!=position and distances[position][v]<time}
        for dest in valves:
            maxadd = max(maxadd, search(distances, time-1-distances[position][dest], dest, valves))
        return flow+maxadd
    distances,valves = problem_input
    valves['AA'] = 0
    return search(distances, 31, 'AA', valves)


def star2(problem_input):
    def search(distances, time1,time2, pos1,pos2, valves):
        flow = valves[pos1]*(time1-1) + valves[pos2]*(time2-1)
        valves = {v:r for v,r in valves.items() if v not in [pos1,pos2]}
        valves[None] = 0
        maxadd = 0
        for dest1 in [None]+[v for v in valves if distances[pos1][v]<time1]:
            for dest2 in [None]+[v for v in valves if v!=dest1 and distances[pos2][v]<time2]:
                if not pos1 and not pos2:
                    continue
                maxadd = max(
                    maxadd,
                    search(
                        distances,
                        *(time1-1-distances[pos1][dest1],time2-1-distances[pos2][dest2]),
                        *(dest1,dest2),
                        valves
                    )
                )
        return flow+maxadd
    distances,valves = problem_input
    valves['AA'] = 0
    return search(distances, *(27,27), *('AA','AA'), valves)


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    #print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
