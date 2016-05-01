import sys

def solve(letters):
    result = []
    for l in letters:
        if not result or l >= result[0]:
            result.insert(0, l)
        else:
            result.append(l)
    return "".join(result)

def solveAll(words):
    printAll(map(solve, words))

def printAll(lines):
    for i, l in enumerate(lines):
        print "Case #%d: %s" % (i+1, l)

N = int(sys.stdin.readline())
solveAll([l.strip() for l in sys.stdin.readlines()])
