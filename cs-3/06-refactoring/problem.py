# Refactor the code for these functions to make it better
# You'll find **lots** of room for improvement

import math

# ---------------------------------------------------------
# Hint: simplify


def sign(num):
    if num > 0 == True:
        return "positive"

    elif num < 0 == True:
        return "negative"

    elif num == 0 == True:
        return "zero"


print(sign(8))
print(sign(0))
print(sign(-7))

# ---------------------------------------------------------
# Hint: format strings


def priceTag(a, b):
    return "A " + a + " costs $" + str(b)


print(priceTag("banana", 10))

# ---------------------------------------------------------
# Hint: if expression


def canVote(age):
    if age >= 18:
        return "can vote"

    return "cannot vote"


print(canVote(5))
print(canVote(18))
print(canVote(50))

# ---------------------------------------------------------
# Hint: min and max


def clamp(num, low, high):
    if num < low:
        return low

    if num > high:
        return high

    return num


print(clamp(-7, 0, 10))
print(clamp(7, 0, 10))
print(clamp(17, 0, 10))

# ---------------------------------------------------------
# Hint: modulo


def isEven(num):
    half = num / 2

    if half == round(half):
        return True

    return False


print(isEven(7))
print(isEven(8))

# ---------------------------------------------------------
# Hint: library function


def distance(x1, y1, x2, y2):
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


print(distance(1, 2, 4, 6))

# ---------------------------------------------------------
# Hint: min


def longestWord(words):
    if not words:
        return None

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(longestWord([]))
print(longestWord("friends romans countrymen lend me your ears".split()))

# ---------------------------------------------------------
# Hint: dictionary


def hexToDec(hexStr):
    digitVals = []

    for d in hexStr:
        if d == "0":
            digitVals.append(0)
        if d == "1":
            digitVals.append(1)
        if d == "2":
            digitVals.append(2)
        if d == "3":
            digitVals.append(3)
        if d == "4":
            digitVals.append(4)
        if d == "5":
            digitVals.append(5)
        if d == "6":
            digitVals.append(6)
        if d == "7":
            digitVals.append(7)
        if d == "8":
            digitVals.append(8)
        if d == "9":
            digitVals.append(9)
        if d == "a":
            digitVals.append(10)
        if d == "b":
            digitVals.append(11)
        if d == "c":
            digitVals.append(12)
        if d == "d":
            digitVals.append(13)
        if d == "e":
            digitVals.append(14)
        if d == "f":
            digitVals.append(15)

    result = 0

    for value in digitVals:
        result *= 16
        result += value

    return result


print(hexToDec("1a"))  # Should print 26

# ---------------------------------------------------------
# Hint: set


def areUnique(values):
    for value in values:
        if values.count(value) > 1:
            return False

    return True


print(areUnique([]))
print(areUnique([1, 2, 3]))
print(areUnique([1, 2, 1]))

# ---------------------------------------------------------
# Hint: match


def rpsWinner(player, ai):
    if player == "rock":
        if ai == "rock":
            return "tie"
        if ai == "paper":
            return "ai"
        if ai == "scissors":
            return "player"
    if player == "paper":
        if ai == "rock":
            return "player"
        if ai == "paper":
            return "tie"
        if ai == "scissors":
            return "ai"
    if player == "scissors":
        if ai == "rock":
            return "ai"
        if ai == "paper":
            return "player"
        if ai == "scissors":
            return "tie"


print(rpsWinner("rock", "paper"))
print(rpsWinner("scissors", "paper"))
print(rpsWinner("paper", "paper"))


# ---------------------------------------------------------
# Hint: sorted


def isSorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            return False

    return True


print(isSorted([]))
print(isSorted([1, 2, 2, 3]))
print(isSorted([1, 3, 2, 4]))

# ---------------------------------------------------------
# Hint: isEven, generator expression


def countEvens(numbers):
    count = 0

    for n in numbers:
        half = n / 2

        if half == round(half):
            count = count + 1

    return count


print(countEvens([1, 4, 2, 7, 3, 1]))

# ---------------------------------------------------------
# Hint: join, generator expression


def shout(words):
    result = ""
    index = 0

    while index < len(words):
        result += words[index].upper()
        result += "!"
        index = index + 1

        if index < len(words):
            result += " "

    return result


print(shout(["germantown", "friends", "school"]))
