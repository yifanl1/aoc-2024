import utils
from collections import defaultdict

inp = utils.get_input(2).strip()
sample_inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
# inp = sample_inp

reports = (list(map(int, row.split())) for row in inp.split("\n"))

safe = 0
safe2 = 0

def get_unsafe(report):
    last_level = report[0]
    idx = 1
    for level in report[1:]:
        if not (0 < (level - last_level) <= 3):
            return (idx, idx - 1)
        idx += 1
        last_level = level
    return None

for report in reports:
    for r in (report, report[::-1]):
        unsafe_spots = get_unsafe(r)
        found_safe = False
        if unsafe_spots is None:
            safe += 1
            safe2 += 1
            break
        for idx in unsafe_spots:
            if get_unsafe([*r[:idx], *r[idx+1:]]) is None:
                found_safe = True
                safe2 += 1
                break
        if found_safe:
            break

utils.write_output(safe, day=2, w=True, append=False)
utils.write_output(safe2, day=2, w=True, append=True)