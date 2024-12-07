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
    if n == 0:
        return target == vals[n]
    v = vals[n]
    if target % v == 0:
        if validate(target // v, vals, n - 1, elephantmath):
            return True
    if target >= v:
        if validate(target - v, vals, n - 1, elephantmath):
            return True
    if elephantmath:
        digits = len(str(v))
        end = 10 ** digits
        if target % end == v:
            if validate(target // end, vals, n - 1, elephantmath):
                return True
    return False

ans = 0
ans2 = 0

for row in inp.strip().split("\n"):
    target, rest = row.split(":", maxsplit=1)
    vals = tuple(map(int, rest.split()))
    if validate(int(target), vals, len(vals) - 1, elephantmath=True):
        ans2 += int(target)
        if validate(int(target), vals, len(vals) - 1, elephantmath=False):
            ans += int(target)

utils.write_output(ans, day=7, w=1)
utils.write_output(ans2, day=7, append=1)

e = time.time()
utils.print_time_diff(s, e)