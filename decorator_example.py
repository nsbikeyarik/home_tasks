def my_decorator(func):
    def wrapper(a, b):
        a = '1'
        b = '2'
        print("Something is happening before the function is called.")
        result = func(a, b)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_whee(a, b):
    return f" {a} Whee! {b}"

data = say_whee('a', 'b')
print(data)