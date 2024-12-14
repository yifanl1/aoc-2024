import utils
import re
from collections import defaultdict
import time

_stime =  time.time()

TCoord = tuple[int, int]
TId = int
TCell = set[TId]
TGrid = dict[TCoord, TCell]

def simulate_robot(v: TCoord, p: TCoord, steps: int = 1) -> TCoord:
    px, py = (p[0] +  v[0] * steps) % W, (p[1] +  v[1] * steps) % H
    return (px, py)


def step_grid(grid: TGrid, robots: dict[TId, TCoord], steps: int = 1) -> TGrid:
    grid_ = defaultdict(set)
    for cell, rids in grid.items():
        for rid in rids:
            p_ = simulate_robot(robots[rid], cell, steps)
            grid_[p_].add(rid)
    return grid_

def _repr_cell(cell: TCell) -> str:
    return str(len(cell)) if cell else '.'

def buffer_grid(grid: TGrid) -> str:
    # Assumption: Surely Eric wouldn't ask a question that involves cursed output that requires base 10 offset,
    if max(map(len, grid.values())) > 10:
        return None
    buf_s = ["".join(
        [_repr_cell(grid[c, r]) for c in range(W)]) 
        for r in range(H)
    ]
    return "\n".join(buf_s)


def danger_level(grid: TGrid) -> int:
    q = {(x, y): 0 for x in (0, 1) for y in (0, 1)}
    mH, mW = (H // 2), (W // 2)
    for x in range(W):
        if x == mW:
            continue
        for y in range(H):
            if y == mH:
                continue
            q[x > mW, y > mH] += len(grid[x, y])
    danger = 1; [danger := danger * v for v in q.values()]
    return danger

def _cscore(grid: TGrid):
    s = 1
    for c in range(H):
        s *= 1 + sum(len(grid[r, c]) for r in range(W))
    return s

def _rscore(grid: TGrid):
    s = 1
    for r in range(W):
        s *= 1 + sum(len(grid[r, c]) for c in range(H))
    return s

inp, W, H = utils.get_input(14), 101, 103
robots = {}
grid =  defaultdict(set)

for rid, rdata in enumerate(inp.strip().split("\n")):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", rdata))
    robots[rid] = (vx, vy)
    grid[(px, py)].add(rid)

ans = danger_level(step_grid(grid, robots, 100))
utils.write_output(ans, day=14, w=1)

m, best = float("inf"), -1
for steps in range(H):
    if (s := _cscore(step_grid(grid, robots, steps))) < m:
        best = steps
        m = s
c_offset = best
for jumps in range(W):
    if (s := _rscore(step_grid(grid, robots, (jumps * H) + c_offset))) < m:
        best = (jumps * H) + c_offset
        m = s

utils.write_output(best, day=14, a=1)


_etime =  time.time()
utils.print_time_diff(_stime, _etime)