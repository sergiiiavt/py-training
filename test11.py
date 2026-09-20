
a = 2
b = 2

print(a == b)
print(a is b)

print("#" * 20)

c = [1, 2, 3]
d = [1, 2, 3]

print(c == d)
print(c is d)

print("#" * 20)


def find(timeout=10, tags=[]):
    print(tags)
    return tags


find(10)
a = find(10, ["tag1", "tag2"])
print("a", a)
b = find(10, ["tag3", "tag4"])
print("b", b)
find(10)


# def find1(self, timeout=10, tags=None):
#     if tags is None:
#         tags = []


# Demonstration of the mutable default argument bug
def find_buggy(timeout=10, tags=[]):
    tags.append(timeout)  # mutates the shared default list object
    print(tags)
    return tags


find_buggy(10)  # [10]
find_buggy(10)  # [10, 10]  <- previous call's mutation leaked in
find_buggy(10)  # [10, 10, 10]  <- keeps growing across calls
