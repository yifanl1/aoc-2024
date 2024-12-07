import utils 
import time

s = time.time()

inp = utils.get_input(day=4).strip()
sample_inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()
# inp = sample_inp

search_map = inp.split("\n")

dirs = [(1, 1), (-1, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)]


def _find(grid, d, x, y, target="XMAS"):
    l = (len(target) - 1) 
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return 0
    if not (0 <= x + l * d[0] < len(grid) and 0 <= y + l * d[1] < len(grid[0])):
        return 0
    i = 0
    for c_ in target:
        if not grid[x + i * d[0]][y + i * d[1]] == c_:
            return 0
        i += 1
    return 1

def _find2(grid, d, x, y, target="MAS"):
    l = (len(target) - 1)
    d1 = _find(grid, d, x, y, target)
    d2 = _find(grid, (d[0] * -1, d[1]), x + l * d[0], y, target)
    d2p = _find(grid, (d[0], d[1] * -1), x, y + l * d[1], target)
    return min(d1, max(d2, d2p))

ans = 0
ans2 = 0
for x, r in enumerate(search_map):
    for y in range(len(r)):
        ans += sum(_find(search_map, d, x, y) for d in dirs)
        ans2 += sum(_find2(search_map, d, x, y) for d in dirs[:2])

utils.write_output(ans, day=4, w=True, append=False)
utils.write_output(ans2, day=4, w=True, append=True)

e = time.time()
utils.print_time_diff(s, e)