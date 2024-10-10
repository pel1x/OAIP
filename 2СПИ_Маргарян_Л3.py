def main():
    
    # 1 задание 

    # while True:
    #     x = input("Введите строку:")
    #     if x == "":
    #         break
    #     print("Длина этой строки:", len(x))

    # 2 задание

    count = 0

    while True:
        x = float(input("Введите число:"))
        if x > 36.6:
            break
        elif x <= 36.6:
            count += 1
    print("Количество отрицательных чиел:", count)

if __name__ == "__main__":
    main()