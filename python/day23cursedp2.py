import utils
from collections import defaultdict
import itertools as it

# print(interconnected)
interconnected2 = defaultdict(set)
for k1, v in map_.items():
    # print("*" * 80)
    # print(k1, v)
    for k2 in v:
        inter2 = v & map_[k2]
        for k3 in inter:
            inter3 = inter2 & map_[k3]
            for k4 in inter3:
                inter4 = inter3 & map_[k4]
                for k5 in inter4:
                    inter5 = inter4 & map_[k5]
                    for k6 in inter5:
                        inter6 = inter5 & map_[k6]
                        # for k7 in inter6:
                            # inter7 = inter6 & map_[k7]
                            # for k8 in inter7:
                            #    inter8 = inter7 & map_[k8]
                                # for k9 in inter8:
                                #    inter9 = inter8 & map_[k9]
                                # interconnected2[tuple(sorted([k1, k2, k3, k4, k5, k6, k7, k8]))].append(inter8)
                            # interconnected2[tuple(sorted([k1, k2, k3, k4, k5, k6, k7]))].append(inter7)
                        interconnected2[tuple(sorted([k1, k2, k3, k4, k5, k6]))].add(tuple(sorted(inter6)))

print(len(interconnected2))

interconnected3 = defaultdict(set)
for l, candidates in interconnected2.items():
    inter1 = set(l)
    # ll = list(l)
    for candidate in candidates:
        for k2 in candidate:
            inter2 = inter1 & map_[k2]
            for k3 in inter:
                inter3 = inter2 & map_[k3]
                for k4 in inter3:
                    inter4 = inter3 & map_[k4]
                    for k5 in inter4:
                        inter5 = inter4 & map_[k5]
                        # for k6 in inter5:
                            # inter6 = inter5 & map_[k6]
                            # interconnected3[tuple(sorted([*l, k2, k3, k4, k5, k6]))].add(tuple(sorted(inter6)))
                        interconnected3[tuple(sorted([*l, k2, k3, k4, k5]))].add(tuple(sorted(inter5)))
                    # interconnected3[tuple(sorted([*l, k2, k3, k4]))].add(tuple(sorted(inter4)))

print(len(interconnected3))
# for k, v in interconnected3.items():
#     print(k)
