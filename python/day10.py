import utils
from collections import defaultdict
import time; _s = time.time()

inp = utils.get_input(10)
sample_inp = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
# inp = sample_inp

DIRS = (1, -1, 1j, -1j)
TGT = 9

hsets = defaultdict(set)
for x, row in enumerate(inp.strip().split("\n")):
    for y, c in enumerate(row):
        hsets[int(c)].add(x + y * 1j)

fhsets = {k: frozenset(v) for k, v in hsets.items()}

class BlackHole(set):
    def add(self, item):
        pass

def traverse(
    pos: complex,
    hsets: dict[int, frozenset[complex]],
    seen: set[complex],
    h: int = 0
) -> int:
    if h == TGT:
        return 1
    ret = 0
    for d in DIRS:
        pos_ = pos + d
        if pos_ in hsets[h + 1] and pos_ not in seen:
            ret += traverse(pos_, hsets, seen, h + 1)
            seen.add(pos_)
    return ret

ans = sum(traverse(s, fhsets, set()) for s in fhsets[0])
utils.write_output(ans, day=10, w=1)

ans2 = sum(traverse(s, fhsets, BlackHole()) for s in fhsets[0])
utils.write_output(ans2, day=10, a=1)

_e = time.time()
utils.print_time_diff(_s, _e)