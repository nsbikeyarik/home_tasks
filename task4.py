def my_decorator(func):
    def wrapper(a, b):
        print("Do something before the function")
        result = func(a, b)
        print("Do something after the function ")
        return result
    return wrapper

@my_decorator
def my_func(a, b):
    return a * b

data = my_func(10, 11)
print(data)
