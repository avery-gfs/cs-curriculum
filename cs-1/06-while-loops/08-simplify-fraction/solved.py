# Simplify the fraction with the given numerator and denominator.
#
# Example:
#
# Enter numerator: 10
# Enter denominator: 24
# Simplified: 5 / 12
#
# Example:
#
# Enter numerator: 5
# Enter denominator: 50
# Simplified: 1 / 10
#
# Example:
#
# Enter numerator: 7
# Enter denominator: 17
# Simplified: 7 / 17

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))

factor = 2

while factor <= min(num, den):
    if num % factor == 0 and den % factor == 0:
        num //= factor
        den //= factor
    else:
        factor += 1

print(f"Simplified: {num} / {den}")
