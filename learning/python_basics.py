from gettext import find


# Exceptions
print("\n" + "#" * 20 + "\n")


class UserNotFoundError(Exception):
    pass


def get_user(user_id):
    if user_id != 123:
        raise UserNotFoundError("User not found")
    return {"id": 123}


try:
    user = get_user("dasda")
except UserNotFoundError:
    print("User does not exist")

print("\n" + "#" * 20 + "\n")

# range()
print("\n" + "#" * 20 + "\n")

for i in range(5):
    print(i)

print("\n" + "#" * 20 + "\n")

# f-strings and split()
print(f"2 + 3 = {2 + 3}")

arr = "1,2,3".split(",")
print(arr)

print("\n" + "#" * 20 + "\n")

# List references
cart = ["apple"]
cart2 = cart

print("cart = {} cart2 = {}".format(cart, cart2))

cart.append("banana")
print("cart = {} cart2 = {}".format(cart, cart2))

# String indexing and slicing
print("hello[0] = " + "hello"[0])
print("hello[-5] = " + "hello"[-5])
print("hello[1:3] = " + "hello"[1:3])
print("hello[1:] = " + "hello"[1:])
print("hello[1:5:2] = " + "hello"[1:5:2])
print("hello[-5:2] = " + "hello"[-5:2])

print("qqqww-eer-ttt-cc----".strip("-"))
print("qqqww-eer-ttt-cc----".replace("-", ""))

print("qqqww-eer-ttt-cc----"[::2])

print("\n" + "#" * 20 + "\n")

# String search
text = "qqqww-###eer-ttt-cc----"
print("FIND: " + text[text.find("###") + 3:])

print("\n" + "#" * 20 + "\n")

# Multiline strings
msg = """a
b
c
d
d
"""

print(msg.isalpha())  # False because the string contains newline characters.

print(msg)
print(msg.splitlines())
print(msg.splitlines(keepends=True))
print("LENGTH msg: " + str(len(msg)))
print(type(msg))
print(msg.count("d"))

msg_split = msg.split("\n")
print(msg_split)
print("----".join(msg_split))

print(msg.replace("d", "D"))

# Dates
from datetime import date

date = date(2024, 6, 1)
print(type(date))
print(date.day)
print(date.isoformat().split("-"))

# User input and string formatting
x = input("msg: ")
print("{0} Hello \n".format(x))
print("""This is a multi-line
string example.
Hello {0}""".format(x))

age = input("Enter your age: ")
print(int(age) + 5)

print("555".upper())

print(type("555".lower()))

x = 333
print("The value of x is: {0}".format(x))
