def main():

    # 1 задание

    name_film = input("Ведите назнавие вильма:")
    name_cinema = input("Введите название конотеатра:")
    time = input("Ведите время:")
    print(f'Билет на " {name_film} " в " {name_cinema} " на " {time} " забронирован.')

    # 2 задание

    salary = int(input("Зарплата за месяц:"))
    hours = int(input("Количество отработанных в выходные часов:"))
    print('Размер премии:', salary * 0.01 * hours)

    # 3 задание

    sum = int(input("Введите сумму:"))
    print(sum % 10, "- по 1р")
    print(sum % 100 // 10, "- по 10р")
    print(sum % 1000 // 100, "- по 100р")
    print(sum // 1000, "- по 1000р")

    # 4 задание

    text = input("Оцените развлекательный комплекс:")
    print(text.find("весело"))
    print(text.find("увлекательно"))
    print(text.find("развлечения"))

    # 5 задание

    s = input("Введите текст:")
    print("Средняя буква:", s[(len(s) - 1) // 2])

    # 6 задание

    feedback = "Алиса и Вася, большое спасибо за теплый приём!"
    name1 = feedback[0:5]
    name2 = feedback[8:12]
    print("Назначить премию:", name1 + "/" + name2)

    # 7 задание

    a = int(input())
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if a + 3 > len(alphabet):
        alphabet = alphabet * 2
        print(alphabet[a - 1:a + 3])
    else:
        print(alphabet[a - 1:a + 3])

    # 8 задание

    my_list = []
    my_list = [1, 2, 3, 4, 5]

    my_list.append(6)
    my_list.extend([7, 8])
    print(my_list)

    my_list.remove(3)
    print(my_list)
    popped_element = my_list.pop(0)
    print(my_list)
    print(popped_element)

    slice_of_list = my_list[1:4]
    print(slice_of_list)

    # метод reverse
    my_list.reverse()
    print(my_list)

    # через срез
    reversed_list = my_list[::-1]
    print(reversed_list)

    two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(two_dimensional_list)

    element = two_dimensional_list[1][2]
    print(element)

    two_dimensional_list[0][0] = 10
    print(two_dimensional_list)

    my_list.clear()
    print(my_list)

    # 9 задание

    empty_tuple = ()
    print("Пустой кортеж:", empty_tuple)

    filled_tuple = (1, 2, 3, 5.5)
    print("Заполненный кортеж:", filled_tuple)

    # 10 задание

    empty_set = set()
    print(empty_set)

    my_set = {1, 2, 3, 4}
    print(my_set)

    empty_set.add(5)
    empty_set.add(10)
    print(empty_set)

    # 11 задание

    empty_dict = {}
    print("Пустой словарь:", empty_dict)

    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print("Словарь с элементами:", my_dict)

    my_dict["job"] = "Engineer"
    print("После добавления значения 'job':", my_dict)

    removed_value = my_dict.pop("age")
    print("После удаления значения 'age':", my_dict)
    print("Удаленное значение:", removed_value)

    my_dict["city"] = "San Francisco"
    print("После изменения значения 'city':", my_dict)

if __name__ == "__main__":
    main()