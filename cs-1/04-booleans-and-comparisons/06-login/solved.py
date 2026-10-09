username = input("Enter username: ")
password = input("Enter password: ")

# Print True if `username` and `password` for a valid login pair, or False otherwise
#
# Valid login pairs:
#
# username: "avery" password: "1234"
# username: "mohammad" password: "1337codez"

print(
    username == "avery"
    and password == "1234"
    or username == "mohammad"
    and password == "1337codez"
)
