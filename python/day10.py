import time; _s = time.time()

import utils

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

DIRS = [1, -1, 1j, -1j]
TGT = 9


tmap = {}
set_s = set()
set_d = set()
rows = inp.strip().split("\n")
for x, row in enumerate(rows):
    for y, c in enumerate(row):
        tmap[x + y * 1j] = int(c)
        if int(c) == 0:
            set_s.add(x + y * 1j)

def traverse(pos, map_, seen, distinct=True):
    h = map_[pos]
    if h == TGT:
        return 1
    ret = 0
    for d in DIRS:
        pos_ = pos + d
        if map_.get(pos_) == h + 1 and (not distinct or pos_ not in seen):
            seen.add(pos_)
            ret += traverse(pos_, map_, seen, distinct)
    return ret

ans = sum(traverse(s, tmap, set()) for s in set_s)
utils.write_output(ans, day=10, w=1)

ans2 = sum(traverse(s, tmap, set(), False) for s in set_s)
utils.write_output(ans2, day=10, a=1)

_e = time.time()
utils.print_time_diff(_s, _e)