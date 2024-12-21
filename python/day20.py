import utils
from typing import TypeAlias
import time

_s = time.time()

TPos: TypeAlias = tuple[int, int]

inp = utils.get_input(20)
rows = inp.strip().split("\n")
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
CHEAT_LIMIT, THRESHOLD = 20, 100

grid = set()
spos, epos = None, None
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == "#":
            continue
        grid.add((i, j))
        if c == "S":
            spos = ((i, j))
        if c == "E":
            epos = ((i, j))

def traverse(
    grid: set[TPos] = grid, s: TPos = epos
) -> dict[TPos, int]:
    Q, steps, last = [s], {s: 0}, {}
    while Q:
        pos = Q.pop()
        for d in DIRS:
            pos_ = pos[0] + d[0], pos[1] + d[1]
            if pos_ in steps or pos_ not in grid:
                continue
            steps[pos_] = steps[pos] + 1
            last[pos_] = pos
            Q.append(pos_)
    return steps, last
picos, last = traverse()

pos_, path = spos, [spos]
while pos_ != epos:
    pos_ = last[pos_]
    path.append(pos_)

BOUNDS = []
for i in range(-CHEAT_LIMIT, CHEAT_LIMIT + 1):
    for j in range(-CHEAT_LIMIT, CHEAT_LIMIT + 1):
        d = abs(i) + abs(j)
        if d == 0 or d > CHEAT_LIMIT:
            continue
        BOUNDS.append((i, j, d))

ans = ans2 = 0
for p1 in path:
    t1 = picos[p1]
    for i, j, d in BOUNDS:
        p2 = p1[0] + i, p1[1] + j
        if t1 - (picos.get(p2, float("inf")) + d) < THRESHOLD:
            continue
        ans += d == 2
        ans2 += 1
utils.write_output(ans, day=20, w=1)
utils.write_output(ans2, day=20, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 20)