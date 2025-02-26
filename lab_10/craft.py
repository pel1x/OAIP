class Wood:
    def __init__(self, quantity):
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def info(self):
        return f"Wood: {self.quantity} units"

class Stone:
    def __init__(self, quantity):
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def info(self):
        return f"Stone: {self.quantity} units"

class Sword:
    def __init__(self, wood: Wood, stone: Stone):
        self.__wood = wood
        self.__stone = stone
        self.__durability = 100

    def craft(self):
        if self.__wood.quantity >= 1 and self.__stone.quantity >= 2:
            print("Crafting a sword...")
            self.__wood._Wood__quantity -= 1
            self.__stone._Stone__quantity -= 2
            return Sword(self.__wood, self.__stone)
        else:
            print("Not enough resources to craft a sword")
            return None

    def info(self):
        return f"Sword: Durability = {self.__durability}"

def main():
    wood = Wood(1)
    stone = Stone(1)

    print(wood.info())
    print(stone.info())

    sword = Sword(wood, stone).craft()
    if sword:
        print(sword.info())
        print(wood.info())
        print(stone.info())

if __name__ == "__main__":
    main()
