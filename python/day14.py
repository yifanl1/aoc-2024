import utils
import re
from collections import defaultdict
import time

_stime =  time.time()

TCoord = tuple[int, int]
TId = int
TGrid = dict[TCoord, int]


def simulate_robot(v: TCoord, p: TCoord, steps: int = 1) -> TCoord:
    return (p[0] +  v[0] * steps) % W, (p[1] +  v[1] * steps) % H


def step_grid(grid: TGrid, robots: dict[TId, TCoord], steps: int = 1) -> TGrid:
    grid_ = defaultdict(int)
    for cell, rids in grid.items():
        for rid in rids:
            p_ = simulate_robot(robots[rid], cell, steps)
            grid_[p_] += 1
    return grid_


def _repr_cell(cell: int) -> str:
    return str(cell) if cell else '.'


def buffer_grid(grid: TGrid) -> str:
    # Assumption: Surely Eric wouldn't ask a question that involves cursed output that requires base 10 offset,
    if max(grid.values()) >= 10:
        raise ValueError("Eric is evil!")
    buf_s = ["".join(
        [_repr_cell(grid[c, r]) for c in range(W)]) 
        for r in range(H)
    ]
    return "\n".join(buf_s)


def danger_level(grid: TGrid) -> int:
    q = {(x, y): 0 for x in (0, 1) for y in (0, 1)}
    mW, mH = (W // 2), (H // 2)
    for (x, y), v in grid.items():
        if x == mW or y == mH:
            continue
        q[x > mW, y > mH] += v
    return utils.product(q.values())

def _cscore(grid: TGrid, robots: dict[TId, TCoord], step: int) -> int:
    grid_ = step_grid(grid, robots, step)
    return utils.product(1 + sum(grid_[r, c] for r in range(W)) for c in range(H))

def _rscore(grid: TGrid, robots: dict[TId, TCoord], step: int) -> int:
    grid_ = step_grid(grid, robots, step)
    return utils.product(1 + sum(grid_[r, c] for c in range(H)) for r in range(W))

inp, W, H = utils.get_input(14), 101, 103
robots = {}
grid =  defaultdict(set)

for rid, rdata in enumerate(inp.strip().split("\n")):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", rdata))
    robots[rid] = (vx, vy)
    grid[(px, py)].add(rid)

ans = danger_level(step_grid(grid, robots, 100))
utils.write_output(ans, day=14, w=1)

c_ = sorted(range(H), key=lambda i: _cscore(grid, robots, i))[0]
r_ = sorted(range(W), key=lambda i: _rscore(grid, robots, (i * H) + c_))[0]
best = (r_ * H) + c_
utils.write_output(best, day=14, a=1)


_etime =  time.time()
utils.print_time_diff(_stime, _etime)

print(buffer_grid(step_grid(grid, robots, best)))
