# ---------------------------------------------------------


def primeFactors(num):
    results = []
    div = 2

    while div < num:
        if num % div != 0:
            div = div + 1
        else:
            results.append(div)
            num //= div

    results.append(num)
    return results


print(primeFactors(60))
print(primeFactors(100000001))


# ---------------------------------------------------------


def primeFactors(num):
    results = []
    div = 2

    while div < math.sqrt(num):
        if num % div:
            div += 1
        else:
            results.append(div)
            num //= div

    results.append(num)
    return results


print(primeFactors(60))
print(primeFactors(100000001))
