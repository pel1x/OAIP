class ПИТОМЕЦ:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            return f"{self.name} покормлен. Уровень голода: {self.hunger}"
        else:
            return f"{self.name} уже сыт."

    def sleep(self):
        if self.energy < 100:
            self.energy += 20
            return f"{self.name} спит. Уровень энергии: {self.energy}"
        else:
            return f"{self.name} не хочет спать."

    def play(self):
        if self.energy > 10 and self.hunger < 90:
            self.energy -= 10
            self.hunger += 10
            return f"{self.name} играет. Уровень энергии: {self.energy}, уровень голода: {self.hunger}"
        else:
            return f"{self.name} не может играть."
