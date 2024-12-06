import utils
from collections import defaultdict

inp = utils.get_input(day=6)
sample_inp = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
# inp = sample_inp
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0

rows = inp.strip().split("\n")

X = len(rows)
Y = len(rows[0])

# This is abusive, please don't do this
INDICES = {x: {y: 0 for y in range(Y)} for x in range(X)}

pos = None
walls = set()
for x, row in enumerate(rows):
    for y, c in enumerate(row):
        if c == "#":
            walls.add((x, y))
        if c == "^":
            pos = (x, y)
assert pos is not None

def traverse_map(walls, spos):
    seen = {spos}
    seen2 = {(spos, 0)}
    pos = spos
    d = 0
    try:
        while True:
            pos_ = (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1])
            if pos_ in walls:
                d = (d + 1) % 4
                continue
            INDICES[pos_[0]][pos_[1]]
            if (pos_, d) in seen2:
                raise ValueError("BAD")
            seen.add(pos_)
            seen2.add((pos_, d))
            pos = pos_
    except KeyError:
        return seen

ans1 = traverse_map(walls, pos)
utils.write_output(len(ans1), day=6, append=0, w=1)

impossible = 0
for p in ans1:
    if p in walls or p == pos:
        continue
    try: 
        traverse_map(walls.union({p}), pos)
    except ValueError:
        impossible += 1
utils.write_output(impossible, day=6, append=1, w=1)