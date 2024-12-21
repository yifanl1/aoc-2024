import utils
import heapq
from typing import TypeAlias
import time

_s = time.time()

TPos: TypeAlias = tuple[int, int]
TDPos: TypeAlias = tuple[TPos, int]
TGrid: TypeAlias = set[TPos]
TCostDict: TypeAlias = dict[TDPos, int]
TPrevDict: TypeAlias =  dict[TDPos, list[TDPos]]

DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

class PNode:
    def __init__(self, pos: tuple[int, int], d: int, val: int) -> None:
        self.val = val
        self.pos = pos
        self.d = d

    def __repr__(self) -> str:
        return f'({self.pos}, {self.d}), val={self.val}'

    def __lt__(self, other: "PNode") -> bool:
        return self.val < other.val

    def neighbours(self) -> list["PNode"]:
        n = []
        for doffset in (0, 1, 3):
            d_ = (self.d + doffset) % 4
            pos_ = self.pos[0] + DIRS[d_][0], self.pos[1] + DIRS[d_][1]
            n.append(PNode(pos_, d_, self.val + (1001 if doffset else 1)))
        return n

inp = utils.get_input(day=16)
rows = inp.strip().split("\n")
spos, epos, sdir = None, None, 0
grid = set()
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == '#':
            continue
        if c == 'S':
            spos = (i, j)
        if c == 'E':
            epos = (i, j)
        grid.add((i, j))
assert spos is not None and epos is not None

def best_path(grid: TPos, s: PNode, epos: TPos) -> tuple[PNode, TCostDict, TPrevDict]:
    _bestcost, _prev = {(s.pos, s.d): 0}, {}
    Q = [(s, 0)]
    # Just for insertion tiebreaks
    _cnt = 1

    while Q:
        c, _ = heapq.heappop(Q)
        if c.pos == epos:
            break
        for n in c.neighbours():
            if n.pos not in grid:
                continue
            b = _bestcost.get((n.pos, n.d), float('inf'))
            if b < n.val:
                continue
            if b > n.val:
                heapq.heappush(Q, (n, _cnt))
                _cnt += 1
                _bestcost[(n.pos, n.d)] = n.val
                # If we found a better path, reset the prev
                _prev[(n.pos, n.d)] = []
            # Any path to a cell with an equal cost will be a "best" path!
            _prev[(n.pos, n.d)].append((c.pos, c.d))
    # (c, _), v = sorted(filter(lambda x: x[0][0] == epos, _bestcost.items()), key=lambda k: k[1])[0]
    return c, _bestcost, _prev

e, _, sprev = best_path(grid, PNode(spos, sdir, 0), epos)

utils.write_output(e.val, day=16, w=1)
# Backtrack through the paths to all known best nodes until we hit the start
best_nodes = set([(e.pos, e.d)])
to_test = best_nodes
while (spos, sdir) not in best_nodes:
    best_backtrack = set()
    for n in to_test:
        best_backtrack |= set(sprev[n])
    to_test = best_backtrack - best_nodes
    best_nodes |= best_backtrack

uniq_cells = set(pos for pos, d in best_nodes)
utils.write_output(len(uniq_cells), day=16, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 16)