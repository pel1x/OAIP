def main():

    # 1 задание

    x = input("Введите строку:")
    while x != "":
        print("Длина этой строки:", len(x))
        x = input("Введите строку:")

    # 2 задание

    count = 0
    x = float(input("Введите число:"))
    while x < 36.6:
        if x < 0:
            count += 1
        x = float(input("Введите число:"))
    print(count)

    # 3 задание

    m1 = -99999
    m2 = -9999999
    a = float(input())
    while abs(a) < 1000:
        if a > m1:
            m2 = m1 
            m1 = a
        elif a > m2:
            m2 = a
        a = float(input())
    print(int(m2))
    
    # 4 задание

    num = input("Введите числа через пробел: ")
    num_list = num.split(" ")
    num_list = list(map(float, num_list))
    min_num = num_list[0]
    counter = 1
    while counter < len(num_list):
        if num_list[counter] < min_num:
            min_num = num_list[counter]
        counter += 1
    print(min_num)

    # 5 задание

    num = float(input("Введите число: "))
    while num != 0:
        if num % 3 == 0 and num % 7 == 0:
            print("Караул!")
            break
        elif num % 3 == 0 and num % 7 != 0:
            print("Несчастливое")
        elif num % 7 == 0 and num % 3 != 0:
            print("Опасное")
        else:
            print(num)
        num = float(input("Введите число: "))

    # 6 задание

    a = 0
    num = 1
    while num <= 10000:
        if num % num == 0 and num % 1 == 0:
            a += num
            num += 1
        else:
            break
    print(a)

    # 7 задание

    # 8 задание

    word = [input("Введите слово: ")]
    small_word = [word[0]]
    while word[-1] != "стоп":
        if len(word[-1]) < len(small_word[-1]):
            small_word = [word[-1]]
        word.append(input("Введите слово: "))
    print(small_word[0])

    # 9 задание

    num = float(input("Введите число: "))
    operator = input("Введите операцию: ")
    result = num
    while operator != "стоп":
        num = float(input("Введите число: "))
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            result /= num
        elif operator == "**":
            result **= num
        print(result)
        operator = input("Введите операцию: ")

    # 10 задание

    result = ""
    while True:
        word = input("Введите слово или !: ")
        if word == "стоп":
            break
        result += word + " "
        if word == "!":
            result = result[:-3] + "!"
            result += "\n"
    print(result)


if __name__ == "__main__":
    main()
