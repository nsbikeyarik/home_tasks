class Mydecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print("Something is happening before the function is called.")
        result = self.function(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

@Mydecorator
def get_cube(x):
    print(f'Given numbers {x}')
    return x * x * x

print("cube numbers", get_cube(10))





