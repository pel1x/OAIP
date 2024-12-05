def main():

    # 1 задание

    a = ""

    for _ in range(1, 9):
        b = input("Введите число: ")
        a += b
    print(a)

    # 2 задание

    n = int(input('Количество имён: '))
    names = []
    for i in range(n):
        names.append(input('Введите имя: '))
    for i in range(n):
        print(i + 1, '-', names[i])


if __name__ == "__main__":
    main()