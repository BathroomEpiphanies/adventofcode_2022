import collections
import numpy as np


alphabet_string = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_display = np.array([
    list('......##..###...##..###..####.####..##..#..#..###...##.#..#.#....#..#.#..#..##..###...##..###...###..###.#..#.#..#.#..#.#..#.#...#####.'),
    list('.....#..#.#..#.#..#.#..#.#....#....#..#.#..#...#.....#.#.#..#....####.##.#.#..#.#..#.#..#.#..#.#......#..#..#.#..#.#..#.#..#.#...#...#.'),
    list('.....#..#.###..#....#..#.###..###..#....####...#.....#.##...#....#..#.#.##.#..#.#..#.#..#.#..#.#......#..#..#.#..#.#..#..##...#.#...#..'),
    list('.....####.#..#.#....#..#.#....#....#.##.#..#...#.....#.#.#..#....#..#.#..#.#..#.###..#..#.###...##....#..#..#.#..#.#..#.#..#...#...#...'),
    list('.....#..#.#..#.#..#.#..#.#....#....#..#.#..#...#..#..#.#.#..#....#..#.#..#.#..#.#....#.#..#.#.....#...#..#..#..#.#.####.#..#...#..#....'),
    list('####.#..#.###...##..###..####.#.....###.#..#..###..##..#..#.####.#..#.#..#..##..#.....#.#.#..#.###....#...##....##.#..#.#..#...#..####.'),
])


encode_table = {} #collections.defaultdict(lambda:np.array([list('####.')]*6))
decode_table = {} #collections.defaultdict(lambda:'_')
for i,c in enumerate(alphabet_string):
    image = alphabet_display[:,i*5:(i+1)*5]
    encode_table[c] = image
    decode_table[''.join(alphabet_display[:,i*5:(i+1)*5].reshape(-1))] = c
#[print(c,d) for d,c in decode_table.items()]


def decode(display):
    display = np.array(display)
    result = ''
    for pos in range(0,len(display[0]),5):
        result += decode_table[''.join(display[:,pos:pos+5].reshape(-1))]
    return result


def encode(characters):
    return '\n'.join(''.join(r) for r in np.hstack([encode_table[c] for c in characters]))


if __name__ == '__main__':
    print(decode(alphabet_display))
    print(encode(alphabet_string))
