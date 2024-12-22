import utils
from typing import TypeAlias
from collections import defaultdict

TPos: TypeAlias = tuple[int, int]
TState: TypeAlias = tuple[int, int, bool]

inp = utils.get_input(21)
codes = inp.strip().split("\n")

numpad = {c: (j, i) for i, row in enumerate(["789", "456", "123", "_0A"]) for j, c in enumerate(row)}
dirpad = {c: (j, i) for i, row in enumerate(["_^A", "<v>"]) for j, c in enumerate(row)}


def steps(pad: dict[TPos, str], code: list[str], i: int = 1) -> dict[TState, int]:
    px, py = pad["A"]
    bx, by = pad["_"]
    res = defaultdict(int)
    for ch in code:
        nx, ny = pad[ch]
        # Flag moves that go through the void
        void = (nx == bx and py == by) or (px == bx and ny == by)
        # Count the horizontal and vertical moves made
        # Multiply this exact sequence as many times as it happens
        dx, dy, adx, ady = nx - px, ny - py, abs(nx - px), abs(ny - py)
        res[(dx, dy, void)] += i
        px, py = nx, ny
    return res


def calc(code: str, n: int) -> int:
    res = steps(numpad, code)
    for _ in range(n + 1):
        res_ = defaultdict(int)
        for (x, y, void), v in res.items():
            target = []
            if x < 0: target += ["<"] * abs(x)
            if y > 0: target += ["v"] * abs(y)
            if y < 0: target += ["^"] * abs(y)
            if x > 0: target += [">"] * abs(x)
            # Invert the moves to avoid going through the void
            if void: target = target[::-1]
            target.append("A")
            for k_, v_ in steps(dirpad, target, v).items():
                res_[k_] += v_
        res = res_
    return sum(res.values()) * int(code[:3])

ans = ans2 = 0
for code in codes:
    ans += calc(code, 2)
    ans2 += calc(code, 25)
utils.write_output(ans, 21, w=1)
utils.write_output(ans2, 21, a=1)