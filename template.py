import math


def template(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print(None)
        return
    
    perimeter = a + b + c

    s = perimeter / 2
    plochad = math.sqrt(s * (s - a) * (s - b) * (s - c))

    ravnobed = (a == b or b == c or a == c)
    ravnost = (a == b == c)

    print(f"Периметр: {perimeter}")
    print(f"Площадь: {plochad}")
    print(f"Равнобедренный: {'да' if ravnobed else 'нет'}")
    print(f"Равносторонний: {'да' if ravnost else 'нет'}")
