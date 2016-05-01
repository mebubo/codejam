from sys import stdin
from collections import defaultdict
from itertools import chain

def flatten(xss):
    return list(chain.from_iterable(xss))

def solve(ls):
    def countOccs():
        occs = defaultdict(int)
        for i in flatten(ls):
            occs[i] += 1
        return occs
    def oddOccs(occs):
        return [k for (k, v) in occs.items() if v % 2 == 1]
    return sorted(oddOccs(countOccs()))

def solveAll(cases):
    printSolutions(map(solve, cases))

def printSolutions(lines):
    for i, l in enumerate(lines):
        print 'Case #%d: %s' % (i+1, " ".join(map(str, l)))

T = int(stdin.readline())
cases = []
for t in xrange(T):
    N = int(stdin.readline())
    cases.append([map(int, stdin.readline().strip().split()) for _ in xrange(2*N - 1)])
solveAll(cases)

