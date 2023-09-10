class Ab:
    name = 'Yarik'
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def set_cords(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z



class Bc(Ab):
    name = "Kolya"

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def printing(self):
        print("Рисуй Bc")

    def printing1(self):
        print(f'{self.a}, {self.b}, {self.c}, {self.d}')

class Cd(Ab):
    def printing(self):
        print('Рисуй Cd')


pt= Ab(1, 2, 3)
t = Bc(1, 2, 4, 5)
t.printing1()
a= Cd(2, 4, 5)
a.printing()