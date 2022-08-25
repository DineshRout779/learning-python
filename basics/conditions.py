x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


name = "John"
list = ["John", "Rick"]
if name in list:
    print("Your name exists in the list")


statement = False
another_statement = True
if statement is True:
    # do something
    print('here')
    pass
elif another_statement is True:  # else if
    # do something else
    print('there')
    pass
else:
    # do another thing
    pass

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

z = [1, 2, 3]
s = z
print(s == z)  # Prints out True
print(s is z)  # Prints out False

print(not False)  # Prints out True
print((not False) == (False))  # Prints out False
