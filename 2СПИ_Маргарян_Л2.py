def main():

    # 1 задание

    a = input("Введите слово:")

    if a == "Python":
        print("ДА")
    else:
        print("НЕТ")

    # 2 задание

    a = input("Введите слово:")
    b = input("Введите слово:")

    if a == "да" and b == "да":
        print("ВЕРНО")
    elif a == "нет" and b == "нет":
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

    # 3 задание

    a = input("Введите слово:")
    b = input("Введите слово:")
    c = input("Введите слово:")

    if a == "раз" and b == "два" and c == "три" or a == "1" and b == "2" and c == "3":
        print("ГОРИ")
    else:
        print("НЕ ГОРИ")

    # 4 задание

    july_city = input("Введите город:")
    august_city = input("Введите город:")

    if (july_city == "Тула" and august_city != "Пенза" and july_city != august_city) or (july_city != "Тула" and august_city == "Пенза" and july_city != august_city):
        print("ДА")
    else:
        print("НЕТ")

    # 5 задание

    import math

    n = float(input("Введите количество километров:"))
    m = float(input("Введите количество километров, которое спортсмен пробегает за день:"))

    if m <= 0 or n <= 0:
        print("Количество километров за день должно быть положительным числом.")
    else:
        days = math.ceil(n / m)
        print("Спортсмен добежит до финиша на", days, "день.")

    # 6 задание

    num = int(input("Введите трехзначное число:"))
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
    sum = num1 + num3

    if sum % 8 == 0 and num2 != 3:
        print("НЕПОДХОДИТ", sum, num2)
    else:
        print("ПОДХОДИТ:", sum, num2)

    # 7 задание

    product_category = input("Введите категорию товара:")

    if product_category == "продукты":
        price = int(input("Введите цену:"))
        if price < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 >= price < 500:
            print("Как насчёт орехов в шоколаде?")
        elif 500 <= price:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")

    # 8 задание

    product1 = int(input("Цена первого товара:"))
    product2 = int(input("Цена второго товара:"))
    product3 = int(input("Цена третьего товара:"))
    sum = product1 + product2 + product3

    if product1 < product2 < product3:
        print("Акция!")
        print("К оплате:", sum / 2)
    elif product1 > product2 > product3:
        print("Акция!")
        print("К оплате:", sum / 3)
    else:
        print("К оплате:", sum)

    # 9 задание

    before_yesterday = int(input("Введите число покупателей за позавчера:"))
    yesterday = int(input("Введите число покупателей за вчера:"))
    if before_yesterday < yesterday:
        print(
            "Сегодня магазин посетит",
            yesterday + (yesterday - before_yesterday),
            "человек",
        )
    if yesterday < before_yesterday:
        print(
            "Сегодня магазин посетит",
            yesterday - (before_yesterday - yesterday),
            "человек",
        )
    if yesterday == before_yesterday:
        print("Сегодня магазин посетит", yesterday, "человек")

    # 10 задание

    year = int(input("Ведите год:"))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Год високосный")
    else:
        print("Год не является високосным")

    # 11 задание

    x = int(input("Ведите число:"))

    if x % 2 == 0:
        print("Число является четным")
    else:
        print("Число является нечетным")


if __name__ == "__main__":
    main()
