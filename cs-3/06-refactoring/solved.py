import math


def sign(num):
    if num > 0:
        return "positive"

    if num < 0:
        return "negative"

    return "zero"


print(sign(8))
print(sign(0))
print(sign(-7))

# ---------------------------------------------------------


def priceTag(item, price):
    return f"A {item} costs ${price}"


print(priceTag("banana", 10))

# ---------------------------------------------------------


def canVote(age):
    return "can vote" if age >= 18 else "cannot vote"


print(canVote(5))
print(canVote(18))
print(canVote(50))

# ---------------------------------------------------------


def clamp(num, low, high):
    return max(low, min(high, num))


print(clamp(-7, 0, 10))
print(clamp(7, 0, 10))
print(clamp(17, 0, 10))

# ---------------------------------------------------------


def isEven(num):
    return num % 2 == 0


print(isEven(7))
print(isEven(8))

# ---------------------------------------------------------


def distance(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))


print(distance(1, 2, 4, 6))

# ---------------------------------------------------------


def product(numbers):
    result = 1

    for n in numbers:
        result *= n

    return result


print(product([1, 2, 3, 4, 5]))

# ---------------------------------------------------------

hexValues = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def hexToDec(hexStr):
    result = 0

    for d in hexStr:
        result *= 16
        result += hexValues[d]

    return result


print(hexToDec("1a"))

# ---------------------------------------------------------


def areUnique(values):
    return len(set(values)) == len(values)


print(areUnique([]))
print(areUnique([1, 2, 3]))
print(areUnique([1, 2, 1]))

# ---------------------------------------------------------


def rpsWinner(player, ai):
    match (player, ai):
        case ("paper", "paper"):
            return "tie"
        case ("paper", "rock"):
            return "player"
        case ("paper", "scissors"):
            return "ai"
        case ("rock", "paper"):
            return "ai"
        case ("rock", "rock"):
            return "tie"
        case ("rock", "scissors"):
            return "player"
        case ("scissors", "paper"):
            return "player"
        case ("scissors", "rock"):
            return "ai"
        case ("scissors", "scissors"):
            return "tie"


print(rpsWinner("rock", "paper"))
print(rpsWinner("scissors", "paper"))
print(rpsWinner("paper", "paper"))

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

# ---------------------------------------------------------


def isSorted(numbers):
    return numbers == sorted(numbers)


print(isSorted([]))
print(isSorted([1, 2, 2, 3]))
print(isSorted([1, 3, 2, 4]))

# ---------------------------------------------------------


def countEvens(numbers):
    return sum(isEven(n) for n in numbers)


print(countEvens([1, 4, 2, 7, 3, 1]))

# ---------------------------------------------------------


def shout(words):
    return " ".join(word.upper() + "!" for word in words)


print(shout(["germantown", "friends", "school"]))
