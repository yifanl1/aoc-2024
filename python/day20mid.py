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

grid = set()
walls = set()
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
    Q, steps, last = deque([s]), {s: 0}, {}
    while Q:
        pos = Q.popleft()
        for d in DIRS:
            pos_ = pos[0] + d[0], pos[1] + d[1]
            if pos_ in steps or pos_ not in grid:
                continue
            steps[pos_] = steps[pos] + 1
            last[pos_] = pos
            Q.append(pos_)
    return steps, last
picos, last = traverse()

pos_, path = spos, set([spos])
while pos_ != epos:
    pos_ = last[pos_]
    path.add(pos_)

# p1 1411
def cheat_ts(pinit, cstart, t, picos, seen, ctime = 0, climit=20):
    cheats = defaultdict(set)
    if ctime >= climit:
        return cheats
    for d in DIRS:
        p_ = cstart[0] + d[0], cstart[1] + d[1]
        if p_ in seen:
            continue
        # print(t, picos.get(p2, -1))
        dt = t - (picos.get(p_, float("inf"))) - ctime
        # assert ctime == abs(p_[0] - pinit[0]) + abs(p_[1] - pinit[1]), f"{ctime=} {p_=} {pinit=}"
        if dt > 0:
            cheats[dt].add((pinit, p_, ctime))
        seen.add(p_)
        for k, v in cheat_ts(p_, t, picos, seen, ctime + 1, climit).items():
            cheats[k] |= v
    return cheats

p1 = defaultdict(set)
p2 = defaultdict(set)
for pos_ in path:
    print(pos_)
    for t, v in cheat_ts(pos_, pos_, picos[pos_], picos, set([pos_])).items():
        p1[t] |= set(v_ for v_ in v if v_[2] == 2)
        p2[t] != v

for k in sorted(p1.keys()):
    print(k, len(p1[k]))

print("*" * 80)
for k in sorted(p2.keys()):
    print(k, len(p2[k]))


# ans = ans2 = 0
# for p1 in GRID:
#     for i in range(-20, 21):
#         for j in range(-1 * (20 - abs(i)), 21 - abs(i)):
#             d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
#         if d == 0 or d > 20:
#             continue
#             p2 = p1[0] + i, p1[1] + j
#         if picos[p2] - picos[p1] - d < 100:
#             continue
#         ans += d == 2
#         ans2 += 1
# print(ans)
# print(ans2)


# ans = 0
# for k in sorted(to_cheat.keys()):
#     print(k, len(to_cheat[k]))
#     if k >= 100:
#         ans += len(to_cheat[k])
# print(ans)
# print("*" * 80)
# ans2 = 0
# for k in sorted(to_cheat_2.keys()):
#     print(k, len(to_cheat_2[k]))
#     if k >= 100:
#         ans2 += len(to_cheat_2[k])
# print(ans2)

# print("*" * 80)
# for k in sorted(timesave.keys()):
#     print(k, len(timesave[k]))
# print("*" * 80)
# print(ans)
