def test(result, expected):
    if result != expected:
        print("!!!!! FAIL !!!!!\n")

    else:
        print("----- PASS: -----\n")

    print(result)
    print()


def compress(text):
    if text == "":
        return ""

    result = ""
    current = text[0]
    count = 0

    for c in text:
        if c == current:
            count += 1

        else:
            result += current + str(count)
            current = c
            count = 1

    return result + current + str(count)


test(compress(""), "")
test(compress("a"), "a1")
test(compress("aaabcc"), "a3b1c2")
test(compress("aabaa"), "a2b1a2")
