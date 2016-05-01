import random
import math

def randomCoin(n):
    return "".join(map(str, [1] + [random.choice([0,1]) for _ in range(n-2)] +[1]))

def numbersForCoin(s):
    return [int(s, i) for i in range(2, 11)]

def findDivisor(n):
    i = 2
    sq = math.sqrt(n)
    while i <= 50:
        if n % i == 0:
            return i
        i += 1

def findCoins(size, count):
    result = {}
    while len(result) < count:
        candidate = randomCoin(size)
        divs = map(findDivisor, numbersForCoin(candidate))
        if all(divs):
            result[candidate] = divs
    return result

def printResult(d):
    print 'Case #1:'
    for k, v in d.items():
        print k, " ".join(map(str, v))

printResult(findCoins(32, 500))
# printResult(findCoins(16, 50))
