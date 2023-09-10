class Soda:
    def __init__(self, additive):
        # if isinstance(additive, str):
        #     self.additive = additive
        if type(additive) == str:
            self.additive = additive
        else:
            self.additive = None

    def show_my_drink(self):
        if self.additive:
           print(f"Газировка и {self.additive}")
        else:
           print("Обычная газировка")


drink1 = Soda("aplle")
drink1.show_my_drink()
drink2 = Soda(1)
drink2.show_my_drink()
drink3 = Soda("mint")
drink3.show_my_drink()

