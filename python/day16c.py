import utils
import heapq

DIRS = (1j, -1, -1j, 1)

class PNode:
    def __init__(self, pos: tuple[int, int], d: int, val: int) -> None:
        self.val = val
        self.pos = pos
        self.d = d

    def __repr__(self) -> str:
        return f'(({self.pos.real}, {self.pos.imag}), {self.d}), val={self.val}'

    def __lt__(self, other) -> bool:
        return self.val < other.val

    def neighbours(self) -> list["PNode"]:
        n1 = PNode(self.pos + DIRS[(self.d + 1) % 4], (self.d + 1) % 4, self.val + 1001)
        n2 = PNode(self.pos + DIRS[(self.d + 3) % 4], (self.d + 3) % 4, self.val + 1001)
        n3 = PNode(self.pos + DIRS[self.d], self.d, self.val + 1)
        return [n1, n2, n3]

inp = utils.get_input(day=16)
rows = inp.strip().split("\n")
spos, epos, sdir = None, None, 0
grid = set()
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == '#':
            continue
        if c == 'S':
            spos = i + (j * 1j)
        if c == 'E':
            epos = i + (j * 1j)
        grid.add(i + (j * 1j))
assert spos is not None and epos is not None

_bestcost, _prev = {(spos, sdir): 0}, {}
Q = [PNode(spos, sdir, 0)]
while Q:
    c = heapq.heappop(Q)
    if c.pos == epos:
        break
    for n in c.neighbours():
        if n.pos not in grid:
            continue
        b = _bestcost.get((n.pos, n.d), float('inf'))
        if b < n.val:
            continue
        if b > n.val:
            heapq.heappush(Q, n)
            _bestcost[(n.pos, n.d)] = n.val
            # If we found a better path, reset the prev
            _prev[(n.pos, n.d)] = []
        # Any path to a cell with an equal cost will be a "best" path!
        _prev[(n.pos, n.d)].append((c.pos, c.d))


utils.write_output(c.val, day=16, w=1)
# Backtrack through the paths to all known best nodes until we hit the start
best_nodes = set([(c.pos, c.d)])
while (spos, sdir) not in best_nodes:
    best_backtrack = set()
    for n in best_nodes:
        best_backtrack |= set(_prev[n])
    best_nodes |= best_backtrack

uniq_cells = set(pos for pos, d in best_nodes)
utils.write_output(len(uniq_cells), day=16, a=1)
