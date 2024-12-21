import utils
import time
from collections import defaultdict
_s = time.time()

inp = utils.get_input(8)

def node_diff(a, b):
    assert a != b
    d, div = (a[0] - b[0], a[1] - b[1]), 1
    if d[0] and d[1]:
        div = utils.gcd(d[0], d[1])
        d = (d[0] // div, d[1] // div)
    elif d[0]:
        d, div = (1, 0), d[0]
    elif d[1]:
        d, div = (0, 1), d[1]
    return d, div

def find_antis(a, antennas, m, in_):
    u1, u2 = set(), set()
    for b in antennas:
        if a == b:
            continue
        d, div = node_diff(a, b)
        for i in range(-m, m + 1):
            node_ = (a[0] + d[0] * i, a[1] + d[1] * i)
            if node_ not in in_:
                continue
            if i == div:
                u1.add(node_)
            u2.add(node_)
            node_ = (node_[0] + d[0], node_[1] + d[1])
    return u1, u2


nodes = defaultdict(set)
IN = set()
rows = inp.strip().split("\n")
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        IN.add((i, j))
        nodes[c].add((i, j))
M = max(len(rows), len(rows[0]))

uniq = set()
uniq2 = set()
for type, antennas in nodes.items():
    if type == '.':
        continue
    for a in antennas:
        res = find_antis(a, antennas, m=M, in_=IN)
        uniq |= res[0]
        uniq2 |= res[1]
utils.write_output(len(uniq), day=8, w=1)
utils.write_output(len(uniq2), day=8, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 8)