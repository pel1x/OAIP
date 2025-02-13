class КНОПКА:
    def __init__(self, label, color, size):
        self.label = label
        self.color = color
        self.size = size
        self.is_disabled = False

    def click(self):
        if not self.is_disabled:
            return f"Кнопка '{self.label}' нажата."
        else:
            return "Кнопка отключена."

    def disable(self):
        self.is_disabled = True
        return f"Кнопка '{self.label}' отключена."

    def enable(self):
        self.is_disabled = False
        return f"Кнопка '{self.label}' включена."
