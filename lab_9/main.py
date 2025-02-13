from СУНДУК import СУНДУК
from КНОПКА import КНОПКА
from ПИТОМЕЦ import ПИТОМЕЦ

def main():
    сундук = СУНДУК()
    сундук.add_item("Золотая монета")
    сундук.add_item("Драгоценный камень")
    print(сундук.open())
    print(сундук.random_item())
    print(сундук.close())

    кнопка = КНОПКА("Отправить", "зеленый", "средний")
    print(кнопка.click())
    print(кнопка.disable())
    print(кнопка.click())
    print(кнопка.enable())
    print(кнопка.click())

    питомец = ПИТОМЕЦ("Томми")
    print(питомец.feed())
    print(питомец.play())
    print(питомец.sleep())
    print(питомец.play())

if __name__ == "__main__":
    main()
