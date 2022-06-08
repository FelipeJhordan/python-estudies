def repeater(old_function):
    def new_function(*args, **kwd):
        old_function(*args, **kwd)
        old_function(*args, **kwd)
    return new_function

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)
