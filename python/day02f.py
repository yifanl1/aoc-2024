import utils

reports = [
    list(map(int, row.split())) 
    for row in utils.get_input(day=2).strip().split("\n")
]

# p1
dt = lambda r: {r[i] - r[i + 1] for i in range(len(r) - 1)}
is_safe = lambda r: dt(r) <= {1, 2, 3} or dt(r) <= {-1, -2, -3}
utils.write_output(sum(map(is_safe, reports)), day=2, w=True, append=False)

# p2
split_report = lambda r: [[*r[:i], *r[i+1:]] for i in range(len(r))]
lax_safe = lambda r: max(is_safe(r), max(map(is_safe, split_report(r))))
utils.write_output(sum(map(lax_safe, reports)), day=2, w=True, append=True)