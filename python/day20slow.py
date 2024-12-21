import utils
from collections import deque, defaultdict
from typing import TypeAlias

TPos: TypeAlias = tuple[int, int]

inp = utils.get_input(20)
sample_inp = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
# inp = sample_inp
rows = inp.strip().split("\n")
X, Y = len(rows), len(rows[0])
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

GRID = set()
walls = set()
spos, epos = None, None
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        if c == "#":
            walls.add((i, j))
            continue
        GRID.add((i, j))
        if c == "S":
            spos = ((i, j))
        if c == "E":
            epos = ((i, j))

def traverse(
    cheat: tuple[TPos, TPos] = (),
    *,
    grid: set[TPos] = GRID, 
    spos: TPos = spos, 
    epos: TPos = epos
) -> dict[TPos, int]:
    Q = deque([spos])
    steps = {spos: 0}
    grid_ = grid | set(cheat)
    last = {spos: None}
    while Q:
        pos = Q.popleft()
        s = steps[pos]
        for d in DIRS:
            pos_ = pos[0] + d[0], pos[1] + d[1]
            # print(pos_, pos_ in grid_)
            if pos_ in steps or pos_ not in grid_:
                continue
            last[pos_] = pos
            if pos_ == epos:
                return s + 1, last
            steps[pos_] = s + 1
            Q.append(pos_)
    return None, None
t0, last = traverse()
assert t0 is not None

def inpath(last, to_check, e=epos):
    node = e
    while node != spos:
        if node == to_check:
            return True
        node = last[node]
    return False

path, s_ = {epos: t0}, t0
node = epos
while spos not in path:
    node = last[node]
    s_ -= 1
    path[node] = s_

# 1411
to_cheat = set()
for pos, t in path.items():
    for d in DIRS:
        p1 = pos[0] + d[0], pos[1] + d[1]
        if p1 not in walls:
            continue
        p2 = p1[0] + d[0], p1[1] + d[1]
        if p1 in walls and p2 in path and path[p2] > t:
            to_cheat.add((p1, p2))

ans = 0
print(len(to_cheat))
timesave = defaultdict(list)
for i, tc in enumerate(to_cheat):
    if not i % 100:
        print(i)
    t_, last_ = traverse(tc)
    # if not inpath(last_, tc[1]):
    #     continue
    dt = t0 - t_
    if dt > 0:
        timesave[dt].append(tc)
    if t_ + 100 <= t0:
        ans += 1

print("*" * 80)
for k in sorted(timesave.keys()):
    print(k, len(timesave[k]))
print("*" * 80)
print(ans)