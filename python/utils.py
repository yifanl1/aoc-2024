import requests

from typing import NamedTuple

from collections import defaultdict
import heapq
import itertools
import os
import math

COOKIE = open("../.mycookie", "r").read()

class Point2D(NamedTuple):
    x: int
    y: int

class Point3D(NamedTuple):
    x: int
    y: int
    z: int

class Point4D(NamedTuple):
    x: int
    y: int
    z: int
    w: int


class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)


class PQ:
    REMOVED = "REMOVED"

    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def add(self, task, priority=0):
        """Add a new task or update the priority of an existing task"""
        if task in self.entry_finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = PQ.REMOVED

    def update_priority(self, task, new_priority):
        """Updates a priority of a task. Raise KeyError if not already in queue"""
        self.remove(task)
        self.add(task, priority=new_priority)

    def pop(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not PQ.REMOVED:
                del self.entry_finder[task]
                return priority, task
        raise KeyError("pop from an empty priority queue")

    def has_entries(self):
        return bool(len(self.entry_finder))


def get_input(day):
    path = f"../inputs/{day:02d}.in"
    if not os.path.exists(path):
        headers = {"Cookie": COOKIE, "User-Agent": "yifanl1 AOCUtils"}
        url = f"https://adventofcode.com/2024/day/{day}/input"

        response = requests.get(url, headers=headers)
        with open(path, "w") as in_file:
            in_file.write(response.text)

    with open(path, "r") as in_file:
        return in_file.read()

def write_output(output, day, *, w=False, append=False, a=False):
    if (w or append or a):
        path = f"../outputs/{day:02d}.out"
        mode = "a" if (append or a) else "w"
        with open(path, mode) as outf:
            outf.write(f"{str(output)}\n")
    print(output)

def gcd(a, b):
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    while a % b:
        a, b = b, a % b
    return b

def lcm(a, b):
    return (a * b) // gcd(a, b)


def rsum(a, b):
    # returns a + a + 1 + a + 2 + ... + b - 1
    return (abs(b - a) * (a + b - 1)) // 2

# _LOG2_10 = 3.32192809488736
def int_len(n):
    return math.floor(math.log10(n)) + 1

def hex_to_bin(hexstr):
    bin_repr = bin(int(hexstr, 16))[2:]
    while not len(bin_repr) % 4 == 0:
        bin_repr = "0" + bin_repr
    i = 0
    while hexstr[i] == "0":
        bin_repr = "0000" + bin_repr
        i += 1
    return bin_repr


def tuple_replace(tup, idx, new):
    return tuple(tup[i] if i != idx else new for i in range(len(tup)))

def print_time_diff(s, e):
    dt = (e - s)
    print(f"took {dt * 1000:.2f}ms or {dt * 1000000:.2f}µs")


class Coord2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, o):
        return Coord2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Coord2(self.x - o.x, self.y - o.y)

    def __mul__(self, n):
        return Coord2(self.x * n, self.y * n)

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, o):
        return self.__hash__() == o.__hash__()

    def __neg__(self):
        return self * -1

    def neighbours(self):
        return set(self + d for d in C2DIRS)

    def __repr__(self):
        return f"C({self.x}, {self.y})"
    

C2DIRS = (Coord2(1, 0), Coord2(0, -1), Coord2(-1, 0), Coord2(0, 1))