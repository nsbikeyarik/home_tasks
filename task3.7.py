class TriangleChecker:
    def __init__(self, a, b, c):
        if all([isinstance(a, int), isinstance(b, int), isinstance(c, int)]):
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Wrong')



    def is_triangle(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
            print("Ура, можно построить треугольник")
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            print("C отрицательными числами ничего не выйдет")
        else:
            print("Жаль, но из этого треуголника не сделать")


pt = TriangleChecker(4, 6, 6)
pt.is_triangle()