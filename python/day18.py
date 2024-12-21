import utils
from collections import deque
from typing import TypeAlias, Iterable
import time

_s = time.time()

TPos: TypeAlias = tuple[int, int]

inp, MAX, P1 = utils.get_input(18), 70, 1024
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

rows = inp.strip().split("\n")
MAX_CORRUPTION = len(rows)
GRID = {(i, j): float("inf") for i in range(MAX + 1) for j in range(MAX + 1)}
for i, row in enumerate(rows):
    x, y = map(int, row.split(",", maxsplit=1))
    GRID[(x, y)] = i
spos, epos = (0, 0), (MAX, MAX)

def traverse(
    corruption: int = P1, 
    grid: dict[TPos, int] = GRID, 
    spos: TPos = (0, 0), 
    epos: TPos = (MAX, MAX)
) -> dict[TPos, int]:
    Q = deque([spos])
    steps = {spos: 0}
    while Q:
        pos = Q.popleft()
        if pos == epos:
            break
        s = steps[pos]
        for d in DIRS:
            pos_ = pos[0] + d[0], pos[1] + d[1]
            if pos_ in steps or grid.get(pos_, -1) < corruption:
                continue
            steps[pos_] = s + 1
            Q.append(pos_)
    return steps

steps_p1 = traverse()
assert epos in steps_p1
utils.write_output(steps_p1[epos], day=18, w=1)

# Just do binary search
bmin, bmax = P1, MAX_CORRUPTION
while bmin <= bmax - 1:
    m = (bmin + bmax) // 2
    steps_m = traverse(m)
    if epos in steps_m:
        bmin = m + 1
    else:
        bmax = m
ans2 = rows[m]
utils.write_output(ans2, day=18, a=1)

_e = time.time()

utils.print_time_diff(_s, _e, 18)