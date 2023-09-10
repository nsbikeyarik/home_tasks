class Point:
    color = "black"
    circle = 3

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __del__(self):
        print(f'deleta some program {str(self)}')

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coorts(self):
        return (self.x, self.y)


pt = Point(1, 3)
print(pt.__dict__)
del(pt)

