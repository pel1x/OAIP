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
text = text.lower
if "весело" in text or "увлекательно" in text or "развлечения" in text:
    for i in range(0, len(s)):