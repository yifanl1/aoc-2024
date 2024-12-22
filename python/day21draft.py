import utils

NUM_PAD = {
    "0": {">": "A", "^": "2"},
    "A": {"<": "0", "^": "3"},

    "1": {">": "2", "^": "4"},
    "2": {"v": "0", "<": "1", ">": "3", "^": "5"},
    "3": {"v": "A", "<": "2", "^": "6"},

    "4": {"v": "1", ">": "5", "^": "7"},
    "5": {"v": "2", "<": "4", ">": "6", "^": "8"},
    "6": {"v": "3", "<": "5", "^": "9"},

    "7": {"v": "4", ">": "8"},
    "8": {"v": "5", ">": "9", "<": "7"},
    "9": {"v": "6", "<": "8"},
}
NUM_PAD_MAP = {}
NUM_PAD_MAP_ = {}
for i, s in enumerate(["_0A", "123", "456", "789"]):
    for j, c in enumerate(s):
        if c == "_":
            continue
        NUM_PAD_MAP[c] = (i, j) 
        NUM_PAD_MAP_[(i, j)] = c


DIR_PAD = {
    "<": {">": "v"},
    "v": {"^": "^", "<": "<", ">": ">"},
    ">": {"<": "v", "^": "A"},
    "^": {">": "A", "v": "v"},
    "A": {"<": "^", "v": ">"}
}
DIR_PAD_MAP = {}
DIR_PAD_MAP_ = {}
for i, s in enumerate(["<v>", "_^A"]):
    for j, c in enumerate(s):
        if c == "_":
            # VOID is illegal, prioritize aligning col before row
            continue
        DIR_PAD_MAP[c] = (i, j)
        DIR_PAD_MAP_[(i, j)] = c


def to_dir(fullcode, fullpad, padmap, init="A"):
    curr = init
    cmds = []
    last_move = None
    for target in fullcode:
        rt, ct = padmap[target]
        while curr != target:
            rc, cc = padmap[curr]
            fc = fullpad[curr]
            mv = None
            # print(target, rt, ct, "|", curr, rc, cc)
            if last_move == "^" and rt > rc and "^" in fc: mv = "^"
            if last_move == "v" and rt < rc and "v" in fc: mv = "v"
            if last_move == "<" and ct < cc and "<" in fc: mv = "<"
            if last_move == ">" and ct > cc and ">" in fc: mv = ">"
            if mv is None:
                if rt > rc and "^" in fc: mv = "^"
                elif rt < rc and "v" in fc: mv = "v"
                elif ct < cc and "<" in fc: mv = "<"
                elif ct > cc and ">" in fc: mv = ">"
            # print(curr, target, fc, mv, last_move, abs(ct - cc), abs(rt - rc))
            cmds.append(mv)
            curr = fullpad[curr][mv]
            last_move = mv
        cmds.append("A")
    return "".join(cmds)

# print(to_dir("<A^A>^^AvvvA", DIR_PAD, DIR_PAD_MAP))

inp = utils.get_input(21)
sample_inp = """029A
980A
179A
456A
379A
"""
inp = sample_inp
rows = inp.strip().split("\n")
ans = ans2 = 0

def calc(code, intermediate=2):
    d_ = to_dir(code, NUM_PAD, NUM_PAD_MAP)
    for i in range(intermediate):
        d_ = to_dir(d_, DIR_PAD, DIR_PAD_MAP)
        print(code, i)
    t = int(code[0:3])
    return t * len(d_)

for code in rows:
    print(code)
    ans += calc(code)
    ans2 += calc(code, 5)
print(ans)
print(ans2)

# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# <v<A>A<A>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v<A<AA>^>AvA^<Av>A^Av<<A>^>AvA^Av<<A>^>AAv<A>A^A<A>Av<A<A>^>AAA<Av>A^A