import utils
import time
from collections import defaultdict
s = time.time()

inp = utils.get_input(8)

def node_diff(a, b):
    return (a[0] - b[0], a[1] - b[1])


nodes = defaultdict(set)
INDICES = {}
for i, row in enumerate(inp.strip().split("\n")):
    for j, c in enumerate(row):
        INDICES[(i, j)] = 0
        nodes[c].add((i, j))
del nodes['.']

uniq = set()
uniq2 = set()
for type, antennas in nodes.items():
    for a in antennas:
        uniq2.add(a)
        for b in antennas:
            if a == b:
                continue
            d = node_diff(a, b)
            try:
                node_ = (a[0] + d[0], a[1] + d[1])
                INDICES[node_]
                uniq.add(node_)
                uniq2.add(node_)
                while True:
                    node_ = (node_[0] + d[0], node_[1] + d[1])
                    INDICES[node_]
                    uniq2.add(node_)
            except KeyError:
                continue
utils.write_output(len(uniq), day=8, w=1)
utils.write_output(len(uniq2), day=8, a=1)

e = time.time()
utils.print_time_diff(s, e)