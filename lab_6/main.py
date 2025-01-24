from quarters import quarters
from future import future
from circuit_resistance import circuit_resistance


def main():
    print("Задание №1")
    print("Первый пример:")
    data = [(1, 1), (-1, 2), (-3, -1)]
    for k, v in sorted(quarters(*data).items()):
        print(f'{k}:\t{v}')
    print("Второй пример:")
    data = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
    for k, v in sorted(quarters(*data).items()):
        print(f'{k}:\t{v}')
    print("Задание №2")
    print("Перывй пример:")
    VIN = 3
    mass = [1, 2, 3, 4]
    const = {"charge": 1.6, "alpha": 0.137, "pi": 3.14}
    print(future(*mass, **const))
    print("Второй пример:")
    VIN = 540
    mass = [1, 2, 3, 4, 5]
    const = {"e0": 9, "mu0": 4}
    print(future(*mass, **const))
    print("Задание №3")
    print("Перывй пример:")
    data = [10, 20, 30]
    print(circuit_resistance(*data))
    print("Второй пример:")
    data = [30, 30, 30]
    print(circuit_resistance(*data, connection="parallel"))


if __name__ == '__main__':
    main()
