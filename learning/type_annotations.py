# Examples of type annotations for common Python built-in types.

age: int = 35
print("int:", age)

price: float = 19.99
print("float:", price)

name: str = "John"
print("str:", name)
print("str: " + name)
print(f"str: {name}")

is_active: bool = True
print("bool:", is_active)

numbers: list[int] = [1, 2, 3]
print("list[int]:", numbers)

statuses: set[str] = {"NEW", "DONE", "FAILED"}
print("set[str]:", statuses)

user: tuple[str, int] = ("John", 35)
print("tuple[str, int]:", user)

person: dict[str, int] = {"age": 35}
print("dict[str, int]:", person)

result: None = None
print("None:", result)

user_id: int | str = 123
print("int | str:", user_id)

email: str | None = None
print("str | None:", email)
