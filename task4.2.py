class Decorator:
    def __init__(self):
        pass

    def decorator(func):
        def wrap(a, b):
            print(f"Calling {func.__name__} with args: {a}, {b}")
            result = func(a, b)
            print(f"{func.__name__} returned: {result}")
            return result

        return wrap

    @staticmethod
    @decorator
    def say_whee(x, y):
        return x + y

result = Decorator.say_whee(2, 4)
print("Result:", result)