from __future__ import annotations

import copy
import re


directions = {
    +1+0j: 0,
    +0+1j: 1,
    -1+0j: 2,
    +0-1j: 3,
}


def parse_input(file_handle):
    lines = [l.rstrip() for l in file_handle.readlines()]
    board = {}
    for r,row in enumerate(lines[:-2]):
        for c,g in enumerate(row):
            if g==' ':
                continue
            board[c+r*1j] = {'g':g}
    moves = [int(a) for a in re.findall(r'[0-9]+', lines[-1])]
    rotations = re.findall(r'[RL]', lines[-1])
    path = moves+rotations
    path[::2] = moves
    path[1::2] = rotations
    return board,path


def part1(problem_input):
    board,path = problem_input
    board = copy.deepcopy(board)
    size_r = max(p.imag for p in board)+1
    size_c = max(p.real for p in board)+1
    for p in board:
        for d in directions:
            q = (p.real+d.real)%size_c + (p.imag+d.imag)%size_r*1j
            while q not in board:
                q = (q.real+d.real)%size_c + (q.imag+d.imag)%size_r*1j
            board[p][d] = q if board[q]['g']=='.' else p
    position = min(p.real for p,b in board.items() if p.imag==0 and b['g']=='.')+0j
    heading = 1+0j
    for move in path:
        if isinstance(move, int):
            for _ in range(move):
                position = board[position][heading]
        elif move=='L':
            heading *= -1j
        elif move=='R':
            heading *= 1j
    return int(1000*(position.imag+1) + 4*(position.real+1) + directions[heading])


def part2(problem_input):
    board,path = problem_input
    board = copy.deepcopy(board)
    size_r = max(p.imag for p in board)+1
    size_c = max(p.real for p in board)+1
    for p in board:
        for d in directions:
            board[p][d] = (p+d,1) if p+d in board and board[p+d]['g']=='.' else (p,1)
    #    #A##E#
    #    D#BB#I
    #    #C##F#
    #    #C#   
    #    G#F   
    #    #L#   
    # #G##L#   
    # D#KK#I   
    # #H##J#   
    # #H#      
    # A#J      
    # #E#      
    for i in range(50):
        # A
        a,b = (50+i)+0j , 0+(150+i)*1j
        board[a][+0-1j] = (b,+1j) if board[b]['g']=='.' else (a,1)
        board[b][-1+0j] = (a,-1j) if board[a]['g']=='.' else (b,1)
        # D
        a,b = 50+i*1j , 0+(149-i)*1j
        board[a][-1+0j] = (b,-1 ) if board[b]['g']=='.' else (a,1)
        board[b][-1+0j] = (a,-1 ) if board[a]['g']=='.' else (b,1)
        # E
        a,b = (100+i)+0j , i+199*1j
        board[a][+0-1j] = (b,+1 ) if board[b]['g']=='.' else (a,1)
        board[b][+0+1j] = (a,+1 ) if board[a]['g']=='.' else (b,1)
        # F
        a,b = (100+i)+49*1j , 99+(50+i)*1j
        board[a][+0+1j] = (b,+1j) if board[b]['g']=='.' else (a,1)
        board[b][+1+0j] = (a,-1j) if board[a]['g']=='.' else (b,1)
        # G
        a,b =  50+(50+i)*1j , i+100*1j
        board[a][-1+0j] = (b,-1j) if board[b]['g']=='.' else (a,1)
        board[b][+0-1j] = (a,+1j) if board[a]['g']=='.' else (b,1)
        # I
        a,b = 149+i*1j , 99+(149-i)*1j
        board[a][+1+0j] = (b,-1 ) if board[b]['g']=='.' else (a,1)
        board[b][+1+0j] = (a,-1 ) if board[a]['g']=='.' else (b,1)
        # J
        a,b = (50+i)+149*1j , 49+(150+i)*1j
        board[a][+0+1j] = (b,+1j) if board[b]['g']=='.' else (a,1)
        board[b][+1+0j] = (a,-1j) if board[a]['g']=='.' else (b,1)
    
    position = 50+0j
    heading = 1+0j
    for move in path:
        if isinstance(move, int):
            for _ in range(move):
                position,heading = board[position][heading][0], heading*board[position][heading][1]
                move -= 1
        elif move=='L':
            heading *= -1j
        elif move=='R':
            heading *= 1j
    return int(1000*(position.imag+1) + 4*(position.real+1) + directions[heading])
