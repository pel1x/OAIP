def main():

    # # 1 задание
    
    # a = input("Введите слово:")
    
    # if a == "Python":
    #     print("ДА")
    # else:
    #     print("НЕТ")
    
    # # 2 задание
    
    # a = input("Введите слово:")
    # b = input("Введите слово:")
    
    # if a == "да" and b == "да":
    #     print("ВЕРНО")
    # elif a == "нет" and b == "нет":
    #     print("ВЕРНО")
    # else:
    #     print("НЕВЕРНО")
    
    # # 3 задание
    
    # a = input("Введите слово:")
    # b = input("Введите слово:")
    # c = input("Введите слово:")
    
    # if a == "раз" and b == "два" and c == "три":
    #     print("ГОРИ")
    # elif a == "1" and b == "2" and c == "3":
    #     print("ГОРИ")
    # else:
    #     print("НЕ ГОРИ")
    
    # # 4 задание
    
    # city1 = input("Введите город:")
    # city2 = input("Введите город:")
    
    # if city1 == "Тула" or city2 == "Пенза":
    #     print("ДА")
    # else:
    #     print("НЕТ")
    
    # # 5 задание
    
    # n = int(input("Сколько нужно пробежать километров:"))
    # m = int(input("Сколько пробегает cпортсмен за день:"))
    
    # if n and m != 0:
    #     d = n // m
    #     print("День:", d)

    # # 6 задание

    # num = int(input("Введите трехзначное число:"))
    # num1 = num // 100
    # num2 = num // 10 % 10
    # num3 = num % 10
    # sum = num1 + num3

    # if sum % 8 == 0 and num2 != 3:
    #     print("НЕПОДХОДИТ", sum, num2)
    # else:
    #     print("ПОДХОДИТ:", sum, num2)
    
    # 7 задание
    
    product_category = input("Введите категорию товара: ")
    
    if product_category == "продукты":
        price = int(input("Введите цену: "))
        if price < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 >= price < 500:
            print("Как насчёт орехов в шоколаде?")
        elif 500 >= price:
            print("Попробуйте экзотические фрукты!")
        else:
            print("Пожалуйста введите корректную цену: ")
    else:
        print("Загляните в товары для дома!")


if __name__ == "__main__":
    main()