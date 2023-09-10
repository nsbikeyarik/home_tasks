def cheak_arg(func):
    def wrapper(x, y, z):
        if all([isinstance(x, int), isinstance(y, int), isinstance(z, int)]):
            print("Good")
            return func(x, y, z)
        else:
            print("Bad")
    return wrapper

@cheak_arg
def sum(x, y, z):
    return (x + y + z)

result = sum(1, 2, 3)
print(result)