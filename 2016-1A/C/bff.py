from sys import stdin
from collections import defaultdict
from itertools import chain

def flatten(xxs):
    return list(chain.from_iterable(xxs))

def solve(bffs):
    bffs = [b-1 for b in bffs]
    N = len(bffs)
    def map_bffs(f):
        return filter(None, [f(i) for i in range(N)])
    def find_cycle(n, k=0):
        curr = n
        seen = set()
        cycle = []
        while curr not in seen:
            seen.add(curr)
            cycle.append(curr)
            curr = bffs[curr]
        if curr == cycle[k]:
            return cycle
    cycles = map_bffs(find_cycle)
    uniq_cycles = set(map(lambda x: tuple(sorted(x)), cycles))
    paths = map_bffs(lambda n: find_cycle(n, -2))
    def longest_path_ending_with(n):
        return max(filter(lambda l: l and l[-1] == n, paths), key=len)
    def longest_path_with_pair(pair):
        return flatten(longest_path_ending_with(x)[:-1] for x in pair)
    def biggest_cycle():
        return max(uniq_cycles, key=len)
    def biggest_set_of_paths():
        pairs = filter(lambda x: len(x) == 2, uniq_cycles)
        return flatten(longest_path_with_pair(pair) for pair in pairs)
    return max(len(biggest_cycle()), len(biggest_set_of_paths()))

def solveAll(cases):
    printAll(map(solve, cases))

def printAll(lines):
    for i, l in enumerate(lines):
        print "Case #%d: %s" % (i+1, l)

def main():
    T = int(stdin.readline())
    cases = []
    for t in range(T):
        n = int(stdin.readline())
        bffs = map(int, stdin.readline().split())
        cases.append(bffs)
    solveAll(cases)

main()
