import utils
import time; _s = time.time()

inp = utils.get_input(day=7)
sample_inp = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
# inp = sample_inp

def validate(target: int, vals: tuple[int, ...], n: int, elephantmath: bool = False) -> bool:
    v = vals[n]
    if not n: return target == v
    if v > target: return False
    if elephantmath:
        _d, _m = divmod(target - v, 10 ** utils.int_len(v))
        if not _m and validate(_d, vals, n - 1, elephantmath):
            return True
    _d, _m = divmod(target, v)
    if not _m and validate(_d, vals, n - 1, elephantmath):
        return True
    return validate(target - v, vals, n - 1, elephantmath)

def parse_inp(inp):
    for r in inp.strip().split("\n"):
        target, rest = r.split(":", maxsplit=1)
        vals = tuple(map(int, rest.split()))
        yield (int(target), vals)

ans = sum(t for t, v in parse_inp(inp) if validate(t, v, len(v) - 1, elephantmath=False))
ans2 = sum(t for t, v in parse_inp(inp) if validate(t, v, len(v) - 1, elephantmath=True))

utils.write_output(ans, day=7, w=1)
utils.write_output(ans2, day=7, append=1)

_e = time.time()
utils.print_time_diff(_s, _e)