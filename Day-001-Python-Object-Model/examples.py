import copy


# 1. Object — Value, Type, Identity

x = 42

print("Value:", x)
print("Type:", type(x))
print("Identity:", id(x))
print()


# 2. Names and Bindings

x = 10
y = x

print("x:", x)
print("y:", y)
print("id(x):", id(x))
print("id(y):", id(y))
print()


# 3. Identity

a = [1, 2]
b = a

print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))
print()


# 4. Equality vs Identity

a = [1, 2]
b = [1, 2]

print("a == b:", a == b)
print("a is b:", a is b)
print()


# 5. Rebinding

x = 10
y = x

x = 20

print("x:", x)
print("y:", y)
print()


# 6. Mutation

numbers = [10]

before = id(numbers)

numbers.append(20)

after = id(numbers)

print("numbers:", numbers)
print("Before:", before)
print("After:", after)
print("Identity unchanged:", before == after)
print()


# 7. Aliasing

a = [1, 2]
b = a
c = b

c.append(3)

print("a:", a)
print("b:", b)
print("c:", c)
print("a is b:", a is b)
print("b is c:", b is c)
print()


# 8. Shallow Copy — Simple List

a = [1, 2, 3]
b = a.copy()

print("a:", a)
print("b:", b)
print("a == b:", a == b)
print("a is b:", a is b)
print()


# 9. Shallow Copy — Nested Lists

a = [[1, 2], [3, 4]]
b = a.copy()

print("a is b:", a is b)
print("a[0] is b[0]:", a[0] is b[0])

b[0].append(5)

print("a:", a)
print("b:", b)
print()


# 10. Deep Copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

print("a is b:", a is b)
print("a[0] is b[0]:", a[0] is b[0])
print(b[0][1] is a[0][1])

b[0].append(5)

print("a:", a)
print("b:", b)
print()


# 11. Function Argument — Mutation

def add_item(x):
    print("Inside id(x):", id(x))
    x.append(3)


a = [1, 2]

print("Outside id(a):", id(a))

add_item(a)

print("a:", a)
print()


# 12. Function Argument — Rebinding

def replace(x):
    x = [100]


a = [1, 2]

replace(a)

print("a:", a)
print()


# 13. Mutation + Rebinding

def modify(x):
    x.append(3)
    x = [100]


a = [1, 2]

modify(a)

print("a:", a)
print()


# 14. List +=

a = [1, 2]

before = id(a)

a += [3]

after = id(a)

print("a:", a)
print("Before:", before)
print("After:", after)
print("Same identity:", before == after)
print()


# 15. List +

a = [1, 2]

before = id(a)

a = a + [3]

after = id(a)

print("a:", a)
print("Before:", before)
print("After:", after)
print("Same identity:", before == after)
print()


# 16. Integer +=

a = 10

before = id(a)

a += 5

after = id(a)

print("a:", a)
print("Before:", before)
print("After:", after)
print("Same identity:", before == after)
print()


# 17. List += Inside Function

def change_list(x):
    x += [3]


a = [1, 2]

change_list(a)

print("a:", a)
print()


# 18. Integer += Inside Function

def change_integer(x):
    x += 5


a = 10

change_integer(a)

print("a:", a)
