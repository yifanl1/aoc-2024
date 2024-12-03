import utils

inp = utils.get_input(2).strip()
sample_inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
# inp = sample_inp


def get_unsafe(report):
    last_level = report[0]
    for idx, level in enumerate(report[1:]):
        if (level - last_level) not in {1, 2, 3}:
            return (idx, idx + 1)
        last_level = level
    return None

def test_report(r):
    unsafe_spots = get_unsafe(r)
    if unsafe_spots is None:
        return 1
    for idx in unsafe_spots:
        if get_unsafe([*r[:idx], *r[idx+1:]]) is None:
            return 2
    return 0


results = [0, 0, 0]

reports = tuple(
    list(map(int, row.split())) 
    for row in utils.get_input(day=2).strip().split("\n")
)

for report in reports:
    result = test_report(report)
    if not result:
        result = test_report(report[::-1])
    results[result] += 1

utils.write_output(results[1], day=2, w=True, append=False)
utils.write_output(results[1] + results[2], day=2, w=True, append=True)
