import json
import sys


#class Packet(tuple):
#
#    def __new__ (cls, packet):
#        if isinstance(packet, int):
#            return packet
#        else:
#            return super(Packet, cls).__new__(cls, (Packet(p) for p in packet))
#    
#    def __lt__(self, other):
#        if isinstance(other, int):
#            return super().__lt__((other,))
#        else:
#            return super().__lt__(other)
#    
#    def __le__(self, other):
#        if isinstance(other, int):
#            return super().__le__((other,))
#        else:
#            return super().__le__(other)
#    
#    def __gt__(self, other):
#        if isinstance(other, int):
#            return super().__gt__((other,))
#        else:
#            return super().__gt__(other)
#    
#    def __ge__(self, other):
#        if isinstance(other, int):
#            return super().__ge__((other,))
#        else:
#            return super().__ge__(other)


class Packet:
    
    def __init__(self, packet):
        self.packet = packet
        return
    
    
    def __str__(self):
        return str(self.packet)
    
    
    def __lt__(self, other):
        
        def list_le(l1,l2):
            if isinstance(l1, int) and isinstance(l2, int):
                result = l1<=l2
            else:
                if isinstance(l1, int):
                    l1 = [l1]
                if isinstance(l2, int):
                    l2 = [l2]
                for a,b in zip(l1, l2):
                    if not list_le(a, b):
                        result = False
                        break
                    if list_lt(a, b):
                        result = True
                        break
                else:
                    #print('hej')
                    result = len(l1)<=len(l2)
            #print('list_le', l1, l2, result)
            return result
        
        def list_lt(l1,l2):
            if isinstance(l1, int) and isinstance(l2, int):
                result = l1<l2
            else:
                if isinstance(l1, int):
                    l1 = [l1]
                if isinstance(l2, int):
                    l2 = [l2]
                for a,b in zip(l1, l2):
                    if not list_le(a, b):
                        result = False
                        break
                    if list_lt(a, b):
                        result = True
                        break
                else:
                    result = len(l1)<len(l2)
            #print('list_lt', l1, l2, result)
            return result
        
        #print()
        return list_lt(self.packet, other.packet)
    


def parse_input(file_handle):
    lines = (l.strip() for l in file_handle.readlines())
    return [Packet(json.loads(l)) for l in lines if l]
    

def star1(problem_input):
    pairs = list(zip(problem_input[0::2], problem_input[1::2]))
    output = 0
    for i,(a,b) in enumerate(pairs, 1):
        if a<b:
            output += i
    return output


def star2(problem_input):
    divider_1 = Packet([[2]])
    divider_2 = Packet([[6]])
    packets = problem_input + [divider_1, divider_2]
    packets.sort()
    packets = [str(p) for p in packets]
    #[print(p) for p in packets]
    pos1 = packets.index(str(divider_1))+1
    pos2 = packets.index(str(divider_2))+1
    return pos1*pos2


if __name__=='__main__':
    problem_input = parse_input(sys.stdin)
    print(f'*1: {star1(problem_input)}')
    print(f'*2: {star2(problem_input)}')
