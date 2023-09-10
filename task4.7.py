class CustomClass:
    def __init__(self, data, a, b):
        self.data = data
        self.a = a
        self.b = b

        self.flag = True

    def generator(self):
        while self.flag:
            yield self.data[self.a:self.b]
            self.a += 3
            self.b += 3
            if self.b > len(self.data) - 1:
                self.flag = False


data = '1234567890abcdefg'
pt = CustomClass(data, 0, 3)
pt.generator()
gen1 = pt.generator()

while True:
    try:
        print(next(gen1))
    except StopIteration:
        break













