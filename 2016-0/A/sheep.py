#!/usr/bin/env python

import sys

def digits(number):
    return map(int, list(str(number)))

def checker():
    s = set()
    def add(ds):
        s.update(ds)
        return len(s) >= 10
    return add

def solve(n):
    c = checker()
    count = 1
    while not c(digits(n * count)):
        count += 1
        if count > 10000:
            return 'INSOMNIA'
    return n * count

def process():
    N = long(sys.stdin.readline())
    for l in range(N):
        print 'Case #%d: %s' % (l + 1, solve(long(sys.stdin.readline())))

if __name__ == '__main__':
    process()
