import utils
import time

_s = time.time()

TPos: type = tuple[int, int]
TGrid: type =  dict[TPos, str]

def can_move(grid: TGrid, d: TPos, pos: TPos) -> bool:
    pos_ = pos[0] + d[0], pos[1] + d[1]
    target = grid[pos_]
    if target == '#':
        return False
    if target == 'O' or (target in '[]' and d[0] == 0):
        return can_move(grid, d, pos_)
    if target in '[]':
        pos_r = pos_[0], pos_[1] + (1 if target == '[' else -1)
        return can_move(grid, d, pos_) and can_move(grid, d, pos_r)
    return True

def move(grid: TGrid, d: TPos, pos: TPos, robot_pos: TPos) -> TPos:
    if not can_move(grid, d, pos):
        return robot_pos
    pos_ = pos[0] + d[0], pos[1] + d[1]
    target = grid[pos_]
    if target == 'O' or (target in '[]' and d[0] == 0):
        move(grid, d, pos_, robot_pos)
    elif target in '[]':
        pos_r = pos_[0], pos_[1] + (1 if target == '[' else -1)
        move(grid, d, pos_, robot_pos)
        move(grid, d, pos_r, robot_pos)
        grid[pos_r] = '.'
    grid[pos_], grid[pos] = grid[pos], '.'
    if pos == robot_pos:
        robot_pos = pos_
    return robot_pos

def grid_buf(grid: TGrid, rows: int, cols: int) -> str:
    buf = ["".join([grid[r, c] for c in range(cols)]) for r in range(rows)]
    buf.append("")
    return "\n".join(buf)

DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

inp = utils.get_input(day=15)
inp_grid, inp_moves = inp.strip().split("\n\n", maxsplit=1)
inp_moves = "".join(inp_moves.split())

grid_, rpos_, grid2_, rpos2_ = {}, None, {}, None
rows = inp_grid.split("\n")
X, Y, Y_ = len(rows), len(rows[0]), len(rows[0]) * 2
for i, row in enumerate(rows):
    for j, c in enumerate(row):
        grid_[(i, j)] = c
        if c in ('#', '.'):
            grid2_[(i, j * 2)] = c
            grid2_[(i, j * 2 + 1)] = c
        elif c == '@':
            rpos_ = (i, j)
            rpos2_ = (i, j * 2)
            grid2_[(i, j * 2)] = c
            grid2_[(i, j * 2 + 1)] = '.'
        elif c == 'O':
            grid2_[(i, j * 2)] = '['
            grid2_[(i, j * 2 + 1)] = ']'

for c in inp_moves:
    rpos_ = move(grid_, DIRS[c], rpos_, rpos_)
    rpos2_ = move(grid2_, DIRS[c], rpos2_, rpos2_)

gps = lambda x: 100 * x[0] + x[1]
ans = sum(map(gps, filter(lambda x: grid_[x] == 'O', grid_.keys())))
ans2 = sum(map(gps, filter(lambda x: grid2_[x] == '[', grid2_.keys())))

utils.write_output(ans, day=15, w=1)
utils.write_output(ans2, day=15, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 15)