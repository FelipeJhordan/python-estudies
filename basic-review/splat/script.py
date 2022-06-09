my_list = ["hello", "tim", 4, 5]
my_dict = {"aple": 1, "pear": 2, "orange": 3}

function_args = {"name": "tim", "age": 5}

# * unpack
# ** pack


def test1(name, age):
    print(name, age)


def test2(**kwargs):
    print(kwargs)


def test3(*args):
    print(args)


print(*my_list)
