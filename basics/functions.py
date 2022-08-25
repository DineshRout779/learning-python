def my_function():
    print("Hello From My Function!")


my_function()


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" %
          (username, greeting))


my_function_with_args('Dinesh', "Good noon!")


def sum_two_numbers(a, b):
    return a + b


print(sum_two_numbers(5, 4))
