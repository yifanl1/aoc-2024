import utils
from collections import defaultdict

inp = utils.get_input(day=5)
sample_inp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
# inp = sample_inp

rules, updates = inp.strip().split("\n\n", maxsplit=1)
rules = rules.split("\n")
updates = updates.split("\n")

prereqs = defaultdict(set)
for rule in rules:
    x_, y_ = rule.split("|", maxsplit=1)
    prereqs[int(x_)].add(int(y_))

def is_valid(prereqs, plst):
    m_ = (len(plst) - 1) // 2
    remaining = set(plst)
    for page in plst:
        remaining.remove(page)
        if not remaining <= prereqs[page]:
            return 0
    return plst[m_]

def reorder(prereqs, plst):
    # Relying on the fact that all updates can be ordered in exactly one valid way
    #  This implies that every page in the update should have 
    #  a different number of prereqs pages in the update
    all_pages = set(plst)
    m_ = (len(plst) - 1) // 2
    for page in plst:
        if len(prereqs[page] & all_pages) == m_:
            return page

ans = ans2 = 0
for update in updates:
    plst = list(map(int, update.split(",")))
    v = is_valid(prereqs, plst)
    if v == 0:
        ans2 += reorder(prereqs, plst)
    else:
        ans += v
utils.write_output(ans, day=5, append=False, w=True)
utils.write_output(ans2, day=5, append=True, w=True)