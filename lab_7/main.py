from factorial import factorial
from fibonacci import fibonacci
from glasnye import count_glasnye
from prostoe import prostoe
from max import max

def main():
    print(factorial(5))
    print(fibonacci(5))
    print(count_glasnye("Как у тебя дела с учебой?"))
    print(prostoe(5))
    print(max(num = [3, 5, 2, 8, 1]))


if __name__ == '__main__':
    main()