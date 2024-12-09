import utils
import time
import multiprocessing as mp

s = time.time()

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
DIRS = (-1, 1j, 1, -1j)
rows = inp.strip().split("\n")

# This is abusive, please don't do this
INDICES = {(x + y * 1j): 0 for y in range(len(rows[0])) for x in range(len(rows))}

def traverse_map(walls, spos):
    d, pos, seen, seen_walls = 0, spos, {spos}, set()
    try:
        while True:
            pos_ = pos + DIRS[d]
            if pos_ in walls:
                if (pos_, d) in seen_walls:
                    return None
                seen_walls.add((pos_, d))
                d = (d + 1) % 4
                continue
            INDICES[pos_]
            seen.add(pos_)
            pos = pos_
    except KeyError:
        return seen

pos = None
walls = set()
for x, row in enumerate(rows):
    for y, c in enumerate(row):
        if c == "#":
            walls.add(x + y * 1j)
        if c == "^":
            pos = x + y * 1j
assert pos is not None

def f(p): 
    return int(traverse_map(walls.union({p}), pos) is None)

if __name__ == "__main__":
    mp.freeze_support()

    seen = traverse_map(walls, pos)
    utils.write_output(len(seen), day=6, w=1)

    l = list(seen - (walls | {pos}))
    n = 0
    with mp.Pool(8) as p:
        impossible = sum(p.imap_unordered(f, l, 100))

    utils.write_output(impossible, day=6, append=1)

    e = time.time()
    utils.print_time_diff(s, e)