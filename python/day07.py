import utils
import time

s = time.time()

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

def validate(target, vals, n, elephantmath=False):
    v = vals[n]
    if not n:
        return target == v
    if v > target:
        return False
    if not target % v:
        if validate(target // v, vals, n - 1, elephantmath):
            return True
    if elephantmath:
        if target % 10 ** len(str(v)) == v and validate(target // 10 ** len(str(v)), vals, n - 1, elephantmath):
            return True
    return validate(target - v, vals, n - 1, elephantmath)

def parse_inp(inp):
    rows = []
    for r in inp.strip().split("\n"):
        target, rest = r.split(":", maxsplit=1)
        vals = tuple(map(int, rest.split()))
        rows.append((int(target), vals))
    return rows

rows = parse_inp(inp)
ans = sum(t for t, v in rows if validate(t, v, len(v) - 1, elephantmath=False))
ans2 = sum(t for t, v in rows if validate(t, v, len(v) - 1, elephantmath=True))

utils.write_output(ans, day=7, w=1)
utils.write_output(ans2, day=7, append=1)

e = time.time()
utils.print_time_diff(s, e)