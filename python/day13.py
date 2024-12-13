import utils
import re

button_pattern = re.compile(r'Button .: X\+(\d+), Y\+(\d+)')
prize_pattern = re.compile(r'Prize: X=(\d+), Y=(\d+)')

inp = utils.get_input(13)
sample_inp = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
# inp = sample_inp

def scores(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> int | None:
    d = (ax * by) - (ay * bx)
    dA = (px * by) - (py * bx)
    dB = (py * ax) - (px * ay)
    if not (dA % d or dB % d):
        A, B = dA // d, dB // d
        if min(A, B) < 0:
            return None
        return 3 * A + B
    return None

def parse_inp(inp: str, conversion: int = 0):
    games= inp.strip().split("\n\n")
    game_lst, game2_lst = [], []
    for game in games:
        a, b, p = game.split("\n", maxsplit=2)
        ax, ay = map(int, re.match(button_pattern, a).groups())
        bx, by = map(int, re.match(button_pattern, b).groups())
        px, py = map(int, re.match(prize_pattern, p).groups())
        yield (ax, ay, bx, by, px + conversion, py + conversion)

get_score = lambda x: scores(*x) or 0

ans = sum(map(get_score, parse_inp(inp)))
utils.write_output(ans, day=12, w=1)

ans2 = sum(map(get_score, parse_inp(inp, conversion=10000000000000)))
utils.write_output(ans2, day=12, a=1)