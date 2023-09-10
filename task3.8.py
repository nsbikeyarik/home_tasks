class Nikola:
    def __init__(self, name, age):
        if name == "Николай":
            self.name = name
            self.age = age
        else:
            self.name =f" Я не {name}, а Николай, возвраст {age}"


p1 = Nikola("Nick", 23)
print(p1.name)
p2 = Nikola("Николай", 13)
print(p2.name)