import math


def template(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print(None)
        return

    perimeter = a + b + c

    s = perimeter / 2
    plochad = math.sqrt(s * (s - a) * (s - b) * (s - c))

    ravnobed = ((a == b and b == c and a != c) or (b == c and a == c and a != b) or (a == b and a == c and b != c))
    ravnost = (a == b == c)

    print(f"Периметр: {perimeter}")
    print(f"Площадь: {plochad:.2f}")
    print(f"Равнобедренный: {'да' if ravnobed else 'нет'}")
    print(f"Равносторонний: {'да' if ravnost else 'нет'}")
