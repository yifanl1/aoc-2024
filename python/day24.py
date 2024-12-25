import utils

inp = utils.get_input(24)
# inp = utils.get_input(24, pathoverride="24sample")

wires = {}

wire_in, cmd_in = inp.strip().split("\n\n", maxsplit=1)
for row in wire_in.split("\n"):
    l, r = row.split(":", maxsplit=1)
    wires[l] = int(r)

gates = {}
for gate in cmd_in.split("\n"):
    a1, op_, a2, _, out = gate.split(" ", maxsplit=4)
    gates[out] = (op_, a1, a2)

def apply_op(op, a, b):
    match op:
        case "AND": return a & b
        case "OR": return a | b
        case "XOR": return a ^ b
        case _: raise ValueError("Evil is happening")

def sim_gates(gates, wires):
    wires_ = wires.copy()
    unapplied_gates = gates.copy()
    while unapplied_gates:
        gates_ = {}
        for o, v in unapplied_gates.items():
            if v[1] in wires_ and v[2] in wires_:
                wires_[o] = apply_op(v[0], wires_[v[1]], wires_[v[2]])
            else:
                gates_[o] = v
        unapplied_gates = gates_
    return wires_

def get_val(wires, prefix="z"):
    fval = []
    for k, v in wires.items():
        if k[0] == prefix:
            fval.append((v, k))
    fval.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for v, k in fval:
        ans = ans * 2 + v
    return ans

wires_ = sim_gates(gates, wires)
x, y, z = map(lambda l: get_val(wires_, l), "xyz")
print(z)
error_bits = (x + y) ^ z
print(bin(error_bits))

class Wire():
    def __init__(self, w):
        self.wire = w
        if self.wire[0] in "xy":
            self.l, self.r, self.op = None, None, None
            return
        op_, l, r = gates[w]
        self.l, self.r, self.op = Wire(l), Wire(r), op_

    def all_reqs(self, maxdepth=-1, depth=0):
        if self.wire[0] in "xy":
            return []
        reqs = [f"{'*' * depth}{self.l.wire}"]
        if maxdepth > 0 and depth < maxdepth:
            reqs += self.l.all_reqs(maxdepth, depth+1)
        reqs += [f"{'*' * depth}{self.r.wire}"]
        if maxdepth > 0 and depth < maxdepth:
            reqs += self.r.all_reqs(maxdepth, depth+1)
        return reqs

    def __hash__(self):
        return self.wire

    def __eq__(self, o):
        return self.wire == o.wire

    def __repr__(self):
        return f"Wire {self.wire}"

def get_bad_bits(wires):
    zbits = sum(map(bool, filter(lambda k: k[0] == "z", wires.keys())))
    to_fix = []
    for i in range(zbits):
        if (error_bits >> i) & 1:
            to_fix.append(Wire(f"z{i:02d}"))
            print(i, bin(error_bits >> i))
    print(to_fix)
    for w in to_fix:
        print(w)
        print("\n".join(w.all_reqs(maxdepth=4)))

get_bad_bits(wires_)