import utils

inp = utils.get_input(25)
items = inp.strip().split("\n\n")
keys, locks = [], []

for item in items:
    filled_cells = set(
        (i, j) for i, row in enumerate(item.split("\n")) 
        for j, c in enumerate(row) if c == '#'
    )
    if (0, 0) in filled_cells: locks.append(filled_cells)
    else: keys.append(filled_cells)

ans = sum(not k & l for k in keys for l in locks)
utils.write_output(ans, 25, w=1)
