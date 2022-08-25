class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myObj = MyClass()

print(myObj.variable)


myObj.function()

# new ex


class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number


newObj = NumberHolder(5)

print(newObj.returnNumber())
