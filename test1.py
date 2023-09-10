class Somelist:

    def new_list_int(self, data):
        result = str()
        for x in data:
            if x.isnumeric():
                result = result + x

        return result

data = 'bhjvhj536bhbk234vbhj57jkb1kj3bk4j6vb5h4b7jk56bn3l2b5jk3b7k57'
p = Somelist()
print(p.new_list_int(data))


def my_decorator(func):
    def wrapper(x, y):
        if isinstance(x, int) and isinstance(y, int):
            print(f'{x} and {y} is integer')
            result = func(x, y)
            return result

    return wrapper


@my_decorator
def _sum(x, y):
    return x + y

print(_sum(2, 3))