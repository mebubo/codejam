
#!/usr/bin/python

from sys import stdin

def solve(s):
    letters = list(s)
    result = []
    def removeAll(lts, digit):
        for l in lts:
            letters.remove(l)
        result.append(digit)
    while letters:
        if 'Z' in letters:
            removeAll('ZERO', 0)
        elif 'W' in letters:
            removeAll('TWO', 2)
        elif 'X' in letters:
            removeAll('SIX', 6)
        elif 'G' in letters:
            removeAll('EIGHT', 8)
        elif 'U' in letters:
            removeAll('FOUR', 4)
        else:
            break
    while letters:
        if 'H' in letters:
            removeAll('THREE', 3)
        elif 'F' in letters:
            removeAll('FIVE', 5)
        elif 'O' in letters:
            removeAll('ONE', 1)
        elif 'S' in letters:
            removeAll('SEVEN', 7)
        else:
            break
    while letters:
        if 'N' in letters:
            removeAll('NINE', 9)
    return "".join(map(str, sorted(result)))

def solveAll(numbers):
    printAll(map(solve, numbers))

def printAll(lines):
    for i, l in enumerate(lines):
        print "Case #%d: %s" % (i+1, l)

T = int(stdin.readline())
numbers = [stdin.readline().strip() for _ in range(T)]
solveAll(numbers)