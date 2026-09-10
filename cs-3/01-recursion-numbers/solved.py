def power2(n):
    # Calculate the `2 ** n` recursively, without using the
    # built-in exponentiation functionality

    if n == 0:
        return 1

    return 2 * power2(n - 1)


print(power2(10))  # Should print 1024


def fibonacci(n):
    # Calculate the nth fibonacci number recursively

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Should print 55


def countdown(n):
    # Print each number n through 1 on a single line, separated by spaces

    if n > 0:
        print(n, end=" ")
        countdown(n - 1)
    else:
        print()


countdown(10)  # Should print 10 9 8 7 6 5 4 3 2 1
