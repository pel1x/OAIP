import random

class СУНДУК:
    def __init__(self):
        self.contents = []
        self.is_open = False

    def add_item(self, item):
        self.contents.append(item)

    def open(self):
        if not self.is_open:
            self.is_open = True
            return f"Сундук открыт. Внутри: {self.contents}"
        else:
            return "Сундук уже открыт."

    def close(self):
        if self.is_open:
            self.is_open = False
            return "Сундук закрыт."
        else:
            return "Сундук уже закрыт."

    def random_item(self):
        if self.contents:
            return random.choice(self.contents)
        else:
            return "Сундук пуст."
