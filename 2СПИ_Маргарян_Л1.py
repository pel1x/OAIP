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