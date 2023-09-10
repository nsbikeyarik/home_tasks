class Audi:
    def __init__(self, name, color, engine, price):
        self.name = name
        self.color = color
        self.engine = engine
        self.price = price
        self.sale = 0


    def name1(self):
        print(f'Model Audi {self.name}, color {self.color}, and hase {self.engine} liter of engine, price {self.price} and have {self.sale} % of sale.')

    def sale_price(self):
        price = self.price - ((self.price // 100) * self.sale)
        print(f'The new price with sale {price}.')

    # @property
    # def get_some(self):
    #     return self.color, self.engine, self.price
    #
    # @get_some.setter
    # def set_some(self, color, engine, price):
    #     self.color = color
    #     self.engine = engine
    #     self.price = price
class A3(Audi):
    def __init__(self, name, color, engine, price, sale):
        super().__init__(name, color, engine, price)
        self.sale = sale

class A4(Audi):
    def __init__(self, name, color, engine, price, sale):
        super().__init__(name, color, engine, price)
        self.sale = sale

class A6(Audi):
    def __init__(self, name, color, engine, price, sale):
        super().__init__(name, color, engine, price)
        self.sale = sale

#design patrn factory
class Factory:

    def made_car(self, model, color, engine, price, sale):
        if model=="A3":
            return self.creat_car_a3( model, color, engine, price, sale)
        elif model=="A4":
            return self.creat_car_a4( model, color, engine, price, sale)
        elif model=="A6":
            return self.creat_car_a6( model, color, engine, price, sale)
        else:
            print('No this car')
            raise ValueError("Not this type")



    def creat_car_a3(self, model, color, engine, price, sale):
        return A3(model, color, engine, price, sale)

    def creat_car_a4(self, model, color, engine, price, sale):
        return A4(model, color, engine, price, sale)

    def creat_car_a6(self, model, color, engine, price, sale):
        return A6(model, color, engine, price, sale)


# audi_a3 = A3(3, "black", 1.5, 10000, 5)
# audi_a4 = A4(4, "white", 2.0, 15000, 7)
# audi_a6 = A6(6, "blue", 3.0, 20000, 8)
# audi_a3.name1()
# audi_a4.name1()
# audi_a4.sale_price()
# audi_a6.name1()
# audi_a6.sale_price()
audi_factory = Factory()
new_car = audi_factory.made_car('A6', 'red', 1.8, 9000, 7)
print(new_car.color)
