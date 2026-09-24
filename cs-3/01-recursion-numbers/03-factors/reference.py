def getFactors(n):
    d = 2
    factors = []

    while n > 1:
        if n % d == 0:
            n //= d
            factors.append(d)
        else:
            d += 1

    return factors


def loopNums():
    for n in range(2, 101):
        print(n, getFactors(n))


loopNums()
