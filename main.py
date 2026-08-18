print(f"2 + 3 = {2 + 3}")

arr = '1,2,3'.split(',')
print(arr)

print("#" * 20)

print("hello[0] = " + "hello"[0])
print("hello"[-5])
print("hello"[1:3])
print("hello"[1:])
print("hello"[1:2::]
print("hello"[-5:2])

msg = """a
b
c
d
d
"""

print(msg)
print(type(msg))
print(msg.count('d'))

print(msg.replace('d', 'D'))

from datetime import date
date = date(2024, 6, 1)
print(type(date))
print(date.day)
print(date.isoformat().split('-'))

x=input('msg: ')
print('{0} Hello \n'.format(x))
print("""This is a multi-line
string example.
Hello {0}""".format(x))

age = input('Enter your age: ')
print (int(age) + 5)

print('555'.upper())

print(type('555'.lower()))

x = 333
print('The value of x is: {0}'.format(x))
