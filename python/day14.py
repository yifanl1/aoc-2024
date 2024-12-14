import utils
import re
from collections import defaultdict

inp, W, H = utils.get_input(14), 101, 103
sample_inp = """p=2,4 v=2,-3
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=9,5 v=-3,-3
"""
# inp, W, H = sample_inp, 11, 7

rows = inp.strip().split("\n")

def simulate_robot(v, p, steps=1):
    vx_, vy_ = v
    while vx_ < 0:
        vx_ += W
    while vy_ < 0:
        vy_ += H
    px, py = (p[0] +  vx_ * steps) % W, (p[1] +  vy_ * steps) % H
    return (px, py)


def step_grid(grid, robots, steps=1):
    grid_ = defaultdict(set)
    for cell, rids in grid.items():
        for rid in rids:
            p_ = simulate_robot(robots[rid], cell, steps)
            grid_[p_].add(rid)
    return grid_


def buffer_grid(grid):
    buf_s = []
    # Assumption: Surely Eric wouldn't ask a question that involves cursed output that requires base 10 offset,
    if max(map(len, grid.values())) > 10:
        return None
    for r in range(H):
        buf = [str(len(grid[c, r])) if grid[c, r] else '.' for c in range(W)]
        buf_s.append("".join(buf))
    return "\n".join(buf_s)


robots = {}
init_grid =  defaultdict(set)

for rid, row in enumerate(rows):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", row))
    robots[rid] = (vx, vy)
    init_grid[(px, py)].add(rid)

final_grid = step_grid(init_grid, robots, 100)
q = {(x, y): 0 for x in (0, 1) for y in (0, 1)}
mH, mW = (H // 2), (W // 2)
for r in range(H):
    if r == mH:
        continue
    for c in range(W):
        if c == mW:
            continue
        q[r > mH, c > mW] += len(final_grid[c, r])
ans = 1
for v in q.values():
    ans *= v
utils.write_output(ans, day=14, w=1)

grid_ = init_grid
seen = set()
i = 0
best_candidates = []
with open("../outputs/easter.out", 'w') as f:
    while True:
        pbuf = buffer_grid(grid_)
        if pbuf is None:
            continue
        if pbuf in seen:
            break
        seen.add(pbuf)
        grid_ = step_grid(grid_, robots)
        # Assumption: A christmas tree is connected somewhere
        if "1111111" in pbuf:
            best_candidates.append(i)
        if "1111" in pbuf:
            f.write(f"{i}\n{pbuf}\n\n")
        i += 1

print(f"{best_candidates=}")