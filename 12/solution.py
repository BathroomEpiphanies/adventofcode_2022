from __future__ import annotations

import networkx


def parse_input(file_handle):
    hills = [l.strip() for l in file_handle.readlines()]
    start = None
    end = None
    for r,row in enumerate(hills):
        c = row.find('S')
        if c>=0:
            start = (r,c)
            hills[r] = hills[r].replace('S','a')
        c = row.find('E')
        if c>=0:
            end = (r,c)
            hills[r] = hills[r].replace('E','z')
    hills = [[ord(c) for c in row] for row in hills]
    graph = networkx.DiGraph()
    for r,row in enumerate(hills):
        for c,height in enumerate(row):
            graph.add_node((r,c), height=height)
            if graph.has_node((r-1,c)):
                if hills[r-1][c]-hills[r][c]<=1:
                    graph.add_edge((r,c),(r-1,c))
                if hills[r][c]-hills[r-1][c]<=1:
                    graph.add_edge((r-1,c),(r,c))
            if graph.has_node((r,c-1)):
                if hills[r][c-1]-hills[r][c]<=1:
                    graph.add_edge((r,c),(r,c-1))
                if hills[r][c]-hills[r][c-1]<=1:
                    graph.add_edge((r,c-1),(r,c))
    hills = graph
    return hills,start,end


def part1(problem_input):
    hills,start,end = problem_input
    return networkx.shortest_path_length(hills,start,end)


def part2(problem_input):
    hills,start,end = problem_input
    paths = dict(networkx.single_target_shortest_path_length(hills, end))
    starts = [a for a,b in hills.nodes(data=True) if b['height']==ord('a')]
    all_paths = [paths[a] for a in starts if a in paths]
    return min(all_paths)
