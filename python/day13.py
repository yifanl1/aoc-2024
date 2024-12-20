import utils
import re
import time 

_s = time.time()

inp = utils.get_input(13)
def tokens(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> int | None:
    d = (ax * by) - (ay * bx)
    dA = (px * by) - (py * bx)
    dB = (py * ax) - (px * ay)
    if (dA % d or dB % d):
        return None
    A, B = dA // d, dB // d
    return None if min(A, B) < 0 else 3 * A + B

def parse_inp(inp: str, conversion: int = 0):
    for game in inp.strip().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(r'\d+', game))
        yield (ax, ay, bx, by, px + conversion, py + conversion)

ans = sum(map(lambda x: tokens(*x) or 0, parse_inp(inp)))
utils.write_output(ans, day=13, w=1)

ans2 = sum(map(lambda x: tokens(*x) or 0, parse_inp(inp, conversion=10000000000000)))
utils.write_output(ans2, day=13, a=1)

_e = time.time()
utils.print_time_diff(_s, _e, 13)