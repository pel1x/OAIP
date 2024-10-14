def main():
    
    # 1 задание

    a = ""

    for _ in range(1, 9):
        b = input("Введите число: ")
        a += b
    print(a)

    # 2 задание

    n = int(input("Введите количество имен: "))

    names = []

    for _ in range(n):
        name = input("Введите имя: ")
        names.append(name)

    for i in range(n):
        print(f"{i + 1}. {names[i]}")

    # 3 задание




if __name__ == "__main__":
    main()